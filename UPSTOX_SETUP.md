# Upstox MCP Setup Guide

This guide explains what you need to set up the Upstox MCP (Model Context Protocol) implementation.

## Prerequisites

1. **Upstox Trading Account**
   - An active Upstox trading account
   - Access to Upstox Developer Portal

## Required API Credentials

### 1. Upstox Developer App Registration

To use the Upstox MCP, you need to create a developer app on Upstox:

1. Go to [Upstox Developer Portal](https://developer.upstox.com/)
2. Sign in with your Upstox credentials
3. Create a new app and note down:
   - **API Key** 
   - **API Secret**
   - **Redirect URI** (can be a dummy URL like `http://localhost:8080`)

### 2. Access Token Generation

The Upstox MCP requires an **Access Token** which you get through OAuth2 flow:

#### Method 1: Manual OAuth Flow
1. Construct the authorization URL:
   ```
   https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id={your_api_key}&redirect_uri={your_redirect_uri}
   ```
2. Visit this URL in browser and authorize the app
3. You'll be redirected to your redirect URI with an authorization code
4. Exchange the authorization code for an access token using Upstox API

#### Method 2: Using Upstox Python SDK
```python
import upstox_api

# Configure OAuth2 access token for authorization
configuration = upstox_api.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
```

### 3. Environment Configuration

Create a `.env` file in your project root with:

```bash
# Required - Access Token from OAuth flow
UPSTOX_ACCESS_TOKEN="your_upstox_access_token_here"

# Optional - For OAuth flow automation
UPSTOX_API_KEY="your_api_key"
UPSTOX_API_SECRET="your_api_secret"
UPSTOX_REDIRECT_URI="your_redirect_uri"
```

## Available MCP Tools

Once configured, you'll have access to these tools:

### Core Trading Tools
- `get_historical_data()` - Get historical candlestick data for any stock
- `get_historical_data_multiple_stocks()` - Get historical data for multiple stocks at once
- `get_portfolio()` - Get your portfolio holdings
- `get_positions()` - Get your current trading positions

### Account Management Tools
- `get_user_profile()` - Get your profile information
- `get_funds()` - Get fund and margin details

## Usage Examples

### Getting Historical Data
```python
# Single stock historical data
data = get_historical_data(
    instrument_key="NSE_EQ|INE062A01020",  # Reliance Industries
    interval="1day",
    from_date="2024-01-01",
    to_date="2024-01-31"
)

# Multiple stocks
data = get_historical_data_multiple_stocks(
    instrument_keys=["NSE_EQ|INE062A01020", "NSE_EQ|INE467B01029"],
    interval="1day",
    from_date="2024-01-01", 
    to_date="2024-01-31"
)
```

### Getting Portfolio Information
```python
# Your holdings
holdings = get_portfolio()

# Current positions
positions = get_positions()

# Account funds
funds = get_funds()
```

## Important Notes

### Instrument Keys
Upstox uses specific instrument keys for stocks. Format: `{EXCHANGE}_{SEGMENT}|{ISIN}`
- Example: `NSE_EQ|INE062A01020` for Reliance Industries on NSE Equity

### Rate Limits
- Upstox has API rate limits
- Historical data requests are limited per day
- Real-time data requires websocket connections

### Access Token Expiry
- Access tokens expire and need to be refreshed
- Implement proper token refresh logic for production use
- Current implementation assumes a valid, non-expired token

## Getting Started

1. **Install Dependencies**
   ```bash
   pip install upstox-python-sdk mcp logzero python-dotenv
   ```

2. **Set Up Credentials**
   - Get your API credentials from Upstox Developer Portal
   - Generate an access token through OAuth2 flow
   - Create `.env` file with your access token

3. **Run the MCP Server**
   ```bash
   python upstox_api.py
   ```

4. **Configure in Your MCP Client**
   ```json
   {
       "mcp": {
           "servers": {
               "upstox": {
                   "command": "python",
                   "args": ["upstox_api.py"]
               }
           }
       }
   }
   ```

## Troubleshooting

### Common Issues

1. **"Access token expired"**
   - Generate a new access token through OAuth flow
   - Update your `.env` file

2. **"Invalid instrument key"**
   - Verify the instrument key format
   - Check if the stock is available on the specified exchange

3. **"Historical data not available"**
   - Check date range (weekends/holidays)
   - Verify the stock was trading during the requested period

### Support
- Upstox API Documentation: https://upstox.com/developer/api-documentation/
- Upstox Python SDK: https://github.com/upstox/upstox-python

## Next Steps

With this setup, you can:
1. Integrate Upstox data into your trading analysis
2. Build automated trading strategies
3. Create portfolio monitoring dashboards
4. Perform backtesting with historical data

Remember to test with small amounts and paper trading before live trading!