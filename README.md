# Trading MCP (Model Context Protocol)

This repository contains Model Context Protocol implementations for popular Indian trading platforms:

- **Angel One MCP** - Interact with Angel One's trading APIs
- **Upstox MCP** - Interact with Upstox's trading APIs

Both implementations allow you to get historical data and portfolio information through MCP tools.

## Prerequisites

- Python 3.10
- Trading account with one or both platforms:
  - Angel One trading account with API credentials
  - Upstox trading account with API credentials

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/trading-mcp.git
cd trading-mcp
git submodule update --init --recursive
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
uv pip install -r requirements.txt
```

## Configuration

### Angel One Configuration

1. Create a test_credentials.py file in the root directory with your Angel One credentials:
```python
# test_credentials.py
API_KEY = "your_api_key"
CLIENT_CODE = "your_client_code"
PASSWORD = "your_password"
PIN = "your_pin"
TOKEN = "your_token"  # Optional
```

### Upstox Configuration

1. Create a .env file in the root directory with your Upstox credentials:
```bash
# .env
UPSTOX_ACCESS_TOKEN="your_upstox_access_token_here"
UPSTOX_API_KEY="your_api_key"  # Optional
UPSTOX_API_SECRET="your_api_secret"  # Optional
```

**Note:** For Upstox, you need to obtain an access token through their OAuth2 flow. You can get this from the Upstox Developer Console after authentication.

## Usage

### Angel One MCP Server

1. You can start `api.py` as an MCP server to your MCP client:
```json
{
    "mcp": {
        "servers": {
            "angelone": {
                "command": "/Users/rohandoshi/.local/bin/uv",
                "args": [
                    "--directory",
                    "/Users/rohandoshi/Development/trading-mcp",
                    "run",
                    "api.py"
                ]
            }
        }
    }
}
```

### Upstox MCP Server

1. You can start `upstox_api.py` as an MCP server to your MCP client:
```json
{
    "mcp": {
        "servers": {
            "upstox": {
                "command": "/Users/rohandoshi/.local/bin/uv",
                "args": [
                    "--directory",
                    "/Users/rohandoshi/Development/trading-mcp",
                    "run",
                    "upstox_api.py"
                ]
            }
        }
    }
}
```

## Available Tools

### Angel One Tools
- `get_historical_data()` - Get historical candlestick data for a stock
- `get_historical_data_multiple_stocks()` - Get historical data for multiple stocks
- `get_portfolio()` - Get portfolio holdings

### Upstox Tools
- `get_historical_data()` - Get historical candlestick data for a stock
- `get_historical_data_multiple_stocks()` - Get historical data for multiple stocks
- `get_portfolio()` - Get portfolio holdings
- `get_positions()` - Get current trading positions
- `get_user_profile()` - Get user profile information
- `get_funds()` - Get fund and margin information

## Results
<img width="773" alt="Screenshot 2025-04-29 at 11 35 09 PM" src="https://github.com/user-attachments/assets/a302099b-2a00-41fe-ace0-0fd82e854e56" />
<img width="770" alt="Screenshot 2025-04-29 at 11 37 03 PM" src="https://github.com/user-attachments/assets/90861d78-87b8-4f8a-a660-c5b48de84c42" />

## Testing Your Setup

### Test Upstox Setup
Run the test script to verify your Upstox setup:
```bash
python test_upstox_setup.py
```

### Test Angel One Setup  
```bash
python test_credentials.py
```

## Quick Start

### For Upstox Users
1. Get API credentials from [Upstox Developer Portal](https://developer.upstox.com/)
2. Generate access token through OAuth2 flow
3. Create `.env` file with `UPSTOX_ACCESS_TOKEN`
4. Run: `python upstox_api.py`

### For Angel One Users
1. Get API credentials from Angel One
2. Create `test_credentials.py` with your credentials
3. Run: `python api.py`

See `UPSTOX_SETUP.md` for detailed Upstox setup instructions.

