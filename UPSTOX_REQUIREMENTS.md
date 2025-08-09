# What You Need for Upstox MCP Implementation

## Summary

I've successfully created a complete Upstox MCP (Model Context Protocol) implementation similar to your existing Angel One MCP. Here's what you'll need to get it working:

## Required API Credentials

### 1. Upstox Developer Account Setup
- **Upstox Developer Portal**: https://developer.upstox.com/
- Create a developer app and get:
  - API Key
  - API Secret  
  - Redirect URI (can be dummy like `http://localhost:8080`)

### 2. Access Token (Most Important)
You need to generate an **Access Token** through Upstox's OAuth2 flow:

1. **Authorization URL** (replace `{your_api_key}` and `{your_redirect_uri}`):
   ```
   https://api.upstox.com/v2/login/authorization/dialog?response_type=code&client_id={your_api_key}&redirect_uri={your_redirect_uri}
   ```

2. **Visit this URL** in your browser and authorize the app

3. **Get authorization code** from the redirect URL

4. **Exchange for access token** using Upstox API

## Environment Setup

Create a `.env` file in the project root:
```bash
UPSTOX_ACCESS_TOKEN="your_actual_access_token_here"
```

## Installation & Testing

1. **Install dependencies** (already done in requirements.txt):
   ```bash
   pip install upstox-python-sdk mcp logzero python-dotenv
   ```

2. **Test your setup**:
   ```bash
   python test_upstox_setup.py
   ```

3. **Run the Upstox MCP server**:
   ```bash
   python upstox_api.py
   ```

## Available Tools

Your Upstox MCP will provide these tools:

### Core Trading Data
- `get_historical_data()` - Historical candlestick data for any stock
- `get_historical_data_multiple_stocks()` - Historical data for multiple stocks
- `get_portfolio()` - Your portfolio holdings

### Enhanced Features (vs Angel One)
- `get_positions()` - Current trading positions
- `get_user_profile()` - Your account profile
- `get_funds()` - Available funds and margins

## Key Differences from Angel One

| Feature | Angel One | Upstox |
|---------|-----------|---------|
| Authentication | API Key + TOTP | OAuth2 Access Token |
| Symbol Format | Symbol Token | Instrument Key (e.g., `NSE_EQ\|INE062A01020`) |
| Additional Tools | Basic portfolio/history | + Positions, Profile, Funds |
| Session Management | Login/logout required | Token-based |

## Files Created for You

1. **`upstox_api.py`** - Main Upstox MCP server
2. **`test_upstox_credentials.py`** - Testing utilities
3. **`test_upstox_setup.py`** - Setup verification script
4. **`upstox_credentials_template.py`** - Credentials template
5. **`UPSTOX_SETUP.md`** - Detailed setup guide

## MCP Client Configuration

Add to your MCP client config:
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

## Next Steps

1. **Get Upstox Developer Credentials**
   - Register at https://developer.upstox.com/
   - Create an app, note API Key/Secret

2. **Generate Access Token**
   - Use OAuth2 flow to get access token
   - Add to `.env` file

3. **Test & Run**
   - Run `python test_upstox_setup.py`
   - Start MCP server with `python upstox_api.py`

4. **Optional: Also Setup Angel One**
   - Both can run simultaneously
   - Angel One: `python api.py`
   - Upstox: `python upstox_api.py`

## Support

- **Detailed Setup Guide**: See `UPSTOX_SETUP.md`
- **Upstox API Docs**: https://upstox.com/developer/api-documentation/
- **Test Script**: Run `python test_upstox_setup.py` anytime

The implementation is ready to use once you provide the access token!