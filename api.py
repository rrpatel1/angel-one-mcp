from SmartApi import SmartConnect
import pyotp
from logzero import logger
import os
from dotenv import load_dotenv
from typing import Any
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("angelone-mcp")

# Load environment variables from .env file
load_dotenv()


@mcp.tool()
def get_historical_data(
    exchange: str,
    symboltoken: str,
    interval: str,
    fromdate: str,
    todate: str
) -> Any:
    """
    Get historical candlestick data from Angel One API.

    Args:
        exchange: The exchange code (e.g., "NSE").
        symboltoken: The symbol token for the stock.
        interval: The time interval for the data (e.g., "ONE_MINUTE", "ONE_HOUR", "ONE_DAY").
        fromdate: Start date and time in "YYYY-MM-DD HH:MM" format.
        todate: End date and time in "YYYY-MM-DD HH:MM" format.
    
    Returns: 
        Historical data as a dictionary or None if an error occurs.
    """
    
    # Get historical data
    params = {
        "exchange": exchange,
        "symboltoken": symboltoken,
        "interval": interval,
        "fromdate": fromdate,
        "todate": todate
    }
    
    try:
        historical_data = smart_api.getCandleData(params)
        return historical_data
    except Exception as e:
        logger.exception(f"Historic Api failed: {e}")
        return None
    
@mcp.tool()
def get_portfolio():
    """
    Get portfolio data from the Angel One API.

    Returns:
        Portfolio data as a dictionary or None if an error occurs.
    """
    try:
        return smart_api.allholding()
    except Exception as e:
        logger.exception(f"Portfolio Api failed: {e}")
        return None


def initialize_api(api_key):
    """Initialize the SmartAPI connection with the API key"""
    return SmartConnect(api_key)


def generate_totp(token):
    """Generate TOTP from the provided token"""
    try:
        return pyotp.TOTP(token).now()
    except Exception as e:
        logger.error("Invalid Token: The provided token is not valid.")
        raise e

def login(smart_api, client_id, password, totp, correlation_id=None):
    """Login to the Angel One API and return the session data"""
    if correlation_id:
        data = smart_api.generateSession(client_id, password, totp)
    else:
        data = smart_api.generateSession(client_id, password, totp)
    
    if data['status'] == False:
        logger.error(data)
        return None
    
    return data['data']


def setup_session(smart_api, session_data):
    """Setup session using the tokens from login"""
    auth_token = session_data['jwtToken']
    refresh_token = session_data['refreshToken']
    
    # Get feed token
    feed_token = smart_api.getfeedToken()
    
    # Get user profile
    profile = smart_api.getProfile(refresh_token)
    
    # Generate token (refresh)
    smart_api.generateToken(refresh_token)
    
    return {
        'auth_token': auth_token,
        'refresh_token': refresh_token,
        'feed_token': feed_token,
        'profile': profile
    }


def get_historical_data(smart_api, params):
    """Get historical candlestick data"""
    try:
        return smart_api.getCandleData(params)
    except Exception as e:
        logger.exception(f"Historic Api failed: {e}")
        return None


def logout(smart_api, client_id):
    """Logout from the API"""
    try:
        result = smart_api.terminateSession(client_id)
        logger.info("Logout Successful")
        return result
    except Exception as e:
        logger.exception(f"Logout failed: {e}")
        return None


def main():
    """Main function to demonstrate API workflow"""
    # Get credentials from environment variables
    api_key = os.environ.get('API_KEY')
    client_id = os.environ.get('CLIENT_ID')
    password = os.environ.get('PASSWORD')
    token = os.environ.get('TOTP_TOKEN')
    
    # Initialize API
    global smart_api
    smart_api = initialize_api(api_key)
    
    # Generate TOTP
    totp = generate_totp(token)
    
    # Login and get session data
    session_data = login(smart_api, client_id, password, totp, correlation_id="abcde")
    if not session_data:
        return
    
    # Setup session with tokens
    session_info = setup_session(smart_api, session_data)
    
    # Get historical data
    historic_params = {
        "exchange": "NSE",
        "symboltoken": "3045",
        "interval": "ONE_MINUTE",
        "fromdate": "2021-02-08 09:00", 
        "todate": "2021-02-08 09:16"
    }
    historical_data = get_historical_data(smart_api, historic_params)

    if historical_data:
        logger.info("Historical Data: %s", historical_data)
    else:
        logger.error("Failed to retrieve historical data.")
    
    # Logout
    # logout(smart_api, client_id)


if __name__ == "__main__":
    main()
    mcp.run(transport='stdio')