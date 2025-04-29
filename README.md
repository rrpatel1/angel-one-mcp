# Angel One MCP (Model Context Protocol)

This repository contains the Model Context Protocol implementation for Angel One trading platform, allowing you to interact with Angel One's trading APIs to get history data and get portfolio data.

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

## Results
<img width="773" alt="Screenshot 2025-04-29 at 11 35 09 PM" src="https://github.com/user-attachments/assets/a302099b-2a00-41fe-ace0-0fd82e854e56" />
<img width="770" alt="Screenshot 2025-04-29 at 11 37 03 PM" src="https://github.com/user-attachments/assets/90861d78-87b8-4f8a-a660-c5b48de84c42" />


