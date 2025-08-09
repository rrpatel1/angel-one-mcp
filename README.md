# Angel One MCP (Model Context Protocol) + Upstox (Planned)

This repository contains the Model Context Protocol implementation for Angel One trading platform, with Upstox integration planned for future releases. The MCP allows you to interact with trading APIs to get historical data and portfolio information.

## Prerequisites

- Python 3.10
- Angel One trading account
- API credentials from Angel One

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/angelone-mcp.git
cd angelone-mcp
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

1. Create a test_credentials.py file in the root directory with your Angel One credentials:
```python
# test_credentials.py
API_KEY = "your_api_key"
CLIENT_CODE = "your_client_code"
PASSWORD = "your_password"
PIN = "your_pin"
TOKEN = "your_token"  # Optional
```

## Usage

1. You can start `api.py` as an mcp server to your mcp client
```json
{
    "mcp": {
        "servers": {
            "angleone": {
                "command": "/Users/rohandoshi/.local/bin/uv",
                "args": [
                    "--directory",
                    "/Users/rohandoshi/Development/angelone-mcp",
                    "run",
                    "api.py"
                ]
            },
        }
    }
}
```

## Roadmap & Progress

### Current Status
- ✅ **Angel One Integration**: Fully implemented with historical data and portfolio support
- 🚧 **Upstox Integration**: In progress - planned for future releases

### Upcoming Features
- [ ] **Upstox MCP Support**: Adding Upstox broker integration alongside Angel One
  - Historical data fetching
  - Portfolio management
  - Real-time quotes (planned)
- [ ] **Multi-broker Support**: Unified interface for multiple brokers
- [ ] **Enhanced Documentation**: Comprehensive API documentation
- [ ] **Testing Suite**: Automated tests for all broker integrations

### How to Track Progress
- Check this README for updates on integration status
- See [PROGRESS.md](PROGRESS.md) for detailed development progress and technical notes
- Monitor the repository for new commits and releases
- Open issues for specific broker integration requests

## Results
<img width="773" alt="Screenshot 2025-04-29 at 11 35 09 PM" src="https://github.com/user-attachments/assets/a302099b-2a00-41fe-ace0-0fd82e854e56" />
<img width="770" alt="Screenshot 2025-04-29 at 11 37 03 PM" src="https://github.com/user-attachments/assets/90861d78-87b8-4f8a-a660-c5b48de84c42" />


