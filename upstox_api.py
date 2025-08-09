try:
    import upstox_api
except ImportError:
    print("Warning: upstox_api not available. Please install upstox-python-sdk")
    upstox_api = None

from logzero import logger
import os
from dotenv import load_dotenv
from typing import Any
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("upstox-mcp")

# Load environment variables from .env file
load_dotenv()

# Global Upstox session object
upstox_session = None


@mcp.tool()
def get_historical_data(
    instrument_key: str,
    interval: str,
    from_date: str,
    to_date: str
) -> Any:
    """
    Get historical candlestick data from Upstox API.

    Args:
        instrument_key: The instrument key for the stock (e.g., "NSE_EQ|INE062A01020").
        interval: The time interval for the data (e.g., "1minute", "1day", "1week").
        from_date: Start date in "YYYY-MM-DD" format.
        to_date: End date in "YYYY-MM-DD" format.
    
    Returns: 
        Historical data as a dictionary or None if an error occurs.
    """
    
    if not upstox_api:
        return {"error": "Upstox API not available. Please install upstox-python-sdk"}
    
    global upstox_session
    if not upstox_session:
        logger.error("Upstox session not initialized. Please login first.")
        return None
    
    try:
        # Get historical data using Upstox API
        api_response = upstox_api.HistoryApi().get_historical_candle_data(
            instrument_key=instrument_key,
            interval=interval,
            from_date=from_date,
            to_date=to_date
        )
        return api_response.to_dict() if api_response else None
    except Exception as e:
        logger.exception(f"Historical data API failed: {e}")
        return None


@mcp.tool()
def get_historical_data_multiple_stocks(
    instrument_keys: list[str],
    interval: str,
    from_date: str,
    to_date: str
) -> Any:
    """
    Get historical candlestick data for multiple stocks from Upstox API.

    Args:
        instrument_keys: List of instrument keys for the stocks.
        interval: The time interval for the data (e.g., "1minute", "1day", "1week").
        from_date: Start date in "YYYY-MM-DD" format.
        to_date: End date in "YYYY-MM-DD" format.
    
    Returns:
        List of historical data dictionaries or None if an error occurs.
    """
    
    results = []
    for instrument_key in instrument_keys:
        try:
            data = get_historical_data(instrument_key, interval, from_date, to_date)
            results.append({
                'instrument_key': instrument_key,
                'data': data
            })
        except Exception as e:
            logger.exception(f"Historical data API failed for {instrument_key}: {e}")
            results.append({
                'instrument_key': instrument_key,
                'data': None,
                'error': str(e)
            })
    return results


@mcp.tool()
def get_portfolio():
    """
    Get portfolio holdings from the Upstox API.

    Returns:
        Portfolio data as a dictionary or None if an error occurs.
    """
    global upstox_session
    if not upstox_session:
        logger.error("Upstox session not initialized. Please login first.")
        return None
    
    try:
        api_response = upstox_api.PortfolioApi().get_holdings()
        return api_response.to_dict() if api_response else None
    except Exception as e:
        logger.exception(f"Portfolio API failed: {e}")
        return None


@mcp.tool()
def get_positions():
    """
    Get current positions from the Upstox API.

    Returns:
        Positions data as a dictionary or None if an error occurs.
    """
    global upstox_session
    if not upstox_session:
        logger.error("Upstox session not initialized. Please login first.")
        return None
    
    try:
        api_response = upstox_api.PortfolioApi().get_positions()
        return api_response.to_dict() if api_response else None
    except Exception as e:
        logger.exception(f"Positions API failed: {e}")
        return None


@mcp.tool()
def get_user_profile():
    """
    Get user profile information from the Upstox API.

    Returns:
        User profile data as a dictionary or None if an error occurs.
    """
    global upstox_session
    if not upstox_session:
        logger.error("Upstox session not initialized. Please login first.")
        return None
    
    try:
        api_response = upstox_api.UserApi().get_user_profile()
        return api_response.to_dict() if api_response else None
    except Exception as e:
        logger.exception(f"User profile API failed: {e}")
        return None


@mcp.tool()
def get_funds():
    """
    Get fund and margin information from the Upstox API.

    Returns:
        Funds data as a dictionary or None if an error occurs.
    """
    global upstox_session
    if not upstox_session:
        logger.error("Upstox session not initialized. Please login first.")
        return None
    
    try:
        api_response = upstox_api.UserApi().get_user_fund_margin()
        return api_response.to_dict() if api_response else None
    except Exception as e:
        logger.exception(f"Funds API failed: {e}")
        return None


def initialize_upstox_session():
    """Initialize Upstox session with access token"""
    global upstox_session
    
    try:
        # Get access token from environment variables
        access_token = os.environ.get('UPSTOX_ACCESS_TOKEN')
        
        if not access_token:
            logger.error("UPSTOX_ACCESS_TOKEN not found in environment variables")
            return False
        
        # Configure API client
        configuration = upstox_api.Configuration()
        configuration.access_token = access_token
        
        # Set the configuration for all API instances
        upstox_api.ApiClient(configuration)
        upstox_session = configuration
        
        logger.info("Upstox session initialized successfully")
        return True
        
    except Exception as e:
        logger.exception(f"Failed to initialize Upstox session: {e}")
        return False


def main():
    """Main function to initialize Upstox session and run MCP server"""
    global upstox_session
    
    # Initialize Upstox session
    if not initialize_upstox_session():
        logger.error("Failed to initialize Upstox session. Exiting.")
        return
    
    logger.info("Upstox MCP server initialized successfully")


if __name__ == "__main__":
    try:
        main()
        mcp.run(transport='stdio')
    except Exception as e:
        logger.exception(f"An error occurred: {e}")
    finally:
        mcp.close()
        logger.info("Upstox MCP closed.")