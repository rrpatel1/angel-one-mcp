try:
    import upstox_api
except ImportError:
    print("Warning: upstox_api not available. Please install upstox-python-sdk")
    upstox_api = None

from logzero import logger
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def initialize_upstox_session():
    """Initialize Upstox session with access token"""
    if not upstox_api:
        logger.error("Upstox API not available. Please install upstox-python-sdk")
        return None
        
    try:
        # Get access token from environment variables
        access_token = os.environ.get('UPSTOX_ACCESS_TOKEN')
        
        if not access_token:
            logger.error("UPSTOX_ACCESS_TOKEN not found in environment variables")
            return None
        
        # Configure API client
        configuration = upstox_api.Configuration()
        configuration.access_token = access_token
        
        # Create API client
        api_client = upstox_api.ApiClient(configuration)
        
        logger.info("Upstox session initialized successfully")
        return api_client
        
    except Exception as e:
        logger.exception(f"Failed to initialize Upstox session: {e}")
        return None


def get_user_profile(api_client):
    """Get user profile information"""
    try:
        api_instance = upstox_api.UserApi(api_client)
        api_response = api_instance.get_user_profile()
        return api_response.to_dict()
    except Exception as e:
        logger.exception(f"User profile API failed: {e}")
        return None


def get_holdings(api_client):
    """Get portfolio holdings"""
    try:
        api_instance = upstox_api.PortfolioApi(api_client)
        api_response = api_instance.get_holdings()
        return api_response.to_dict()
    except Exception as e:
        logger.exception(f"Holdings API failed: {e}")
        return None


def get_positions(api_client):
    """Get current positions"""
    try:
        api_instance = upstox_api.PortfolioApi(api_client)
        api_response = api_instance.get_positions()
        return api_response.to_dict()
    except Exception as e:
        logger.exception(f"Positions API failed: {e}")
        return None


def get_funds(api_client):
    """Get fund and margin information"""
    try:
        api_instance = upstox_api.UserApi(api_client)
        api_response = api_instance.get_user_fund_margin()
        return api_response.to_dict()
    except Exception as e:
        logger.exception(f"Funds API failed: {e}")
        return None


def get_historical_data(api_client, instrument_key, interval, from_date, to_date):
    """Get historical candlestick data"""
    try:
        api_instance = upstox_api.HistoryApi(api_client)
        api_response = api_instance.get_historical_candle_data(
            instrument_key=instrument_key,
            interval=interval,
            from_date=from_date,
            to_date=to_date
        )
        return api_response.to_dict()
    except Exception as e:
        logger.exception(f"Historical data API failed: {e}")
        return None


def main():
    """Main function to demonstrate Upstox API workflow"""
    
    # Initialize Upstox session
    api_client = initialize_upstox_session()
    if not api_client:
        return
    
    # Get user profile
    profile_data = get_user_profile(api_client)
    if profile_data:
        logger.info("User Profile: %s", profile_data)
    else:
        logger.error("Failed to retrieve user profile.")
    
    # Get portfolio holdings
    holdings_data = get_holdings(api_client)
    if holdings_data:
        logger.info("Holdings: %s", holdings_data)
    else:
        logger.error("Failed to retrieve holdings.")
    
    # Get positions
    positions_data = get_positions(api_client)
    if positions_data:
        logger.info("Positions: %s", positions_data)
    else:
        logger.error("Failed to retrieve positions.")
    
    # Get funds
    funds_data = get_funds(api_client)
    if funds_data:
        logger.info("Funds: %s", funds_data)
    else:
        logger.error("Failed to retrieve funds.")
    
    # Get historical data (example)
    # Note: Replace with valid instrument key for testing
    historical_params = {
        "instrument_key": "NSE_EQ|INE062A01020",  # Example: RELIANCE
        "interval": "1day",
        "from_date": "2024-01-01",
        "to_date": "2024-01-31"
    }
    
    historical_data = get_historical_data(
        api_client, 
        historical_params["instrument_key"],
        historical_params["interval"],
        historical_params["from_date"],
        historical_params["to_date"]
    )
    
    if historical_data:
        logger.info("Historical Data: %s", historical_data)
    else:
        logger.error("Failed to retrieve historical data.")


if __name__ == "__main__":
    main()