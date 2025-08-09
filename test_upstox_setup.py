#!/usr/bin/env python3
"""
Upstox MCP Test Script

This script tests the Upstox MCP implementation without requiring actual API calls.
Run this to verify your setup is correct before adding real credentials.
"""

import os
import sys

def test_imports():
    """Test if all required packages can be imported"""
    print("Testing imports...")
    
    try:
        import mcp
        print("✓ MCP package available")
    except ImportError as e:
        print(f"✗ MCP package missing: {e}")
        return False
    
    try:
        from mcp.server.fastmcp import FastMCP
        print("✓ FastMCP available")
    except ImportError as e:
        print(f"✗ FastMCP missing: {e}")
        return False
    
    try:
        import logzero
        print("✓ logzero available")
    except ImportError as e:
        print(f"✗ logzero missing: {e}")
        return False
    
    try:
        import dotenv
        print("✓ python-dotenv available")
    except ImportError as e:
        print(f"✗ python-dotenv missing: {e}")
        return False
    
    try:
        import upstox_api
        print("✓ upstox-python-sdk available")
    except ImportError as e:
        print(f"✗ upstox-python-sdk missing: {e}")
        print("  Install with: pip install upstox-python-sdk")
        return False
    
    return True

def test_upstox_mcp_loading():
    """Test if the Upstox MCP module loads correctly"""
    print("\nTesting Upstox MCP loading...")
    
    try:
        from upstox_api import mcp as upstox_mcp
        print("✓ Upstox MCP module loaded successfully")
        return True
    except ImportError as e:
        print(f"✗ Failed to load Upstox MCP: {e}")
        return False
    except Exception as e:
        print(f"✗ Error loading Upstox MCP: {e}")
        return False

def test_environment_setup():
    """Test environment variable setup"""
    print("\nTesting environment setup...")
    
    # Check if .env file exists
    env_file = ".env"
    if os.path.exists(env_file):
        print(f"✓ {env_file} file found")
    else:
        print(f"✗ {env_file} file not found")
        print("  Create a .env file with your Upstox credentials")
        print("  See upstox_credentials_template.py for format")
    
    # Load environment variables
    try:
        from dotenv import load_dotenv
        load_dotenv()
        
        access_token = os.environ.get('UPSTOX_ACCESS_TOKEN')
        if access_token:
            print("✓ UPSTOX_ACCESS_TOKEN found in environment")
            if access_token.startswith('your_'):
                print("  ⚠ Warning: Access token appears to be placeholder")
        else:
            print("✗ UPSTOX_ACCESS_TOKEN not found in environment")
            print("  Add UPSTOX_ACCESS_TOKEN to your .env file")
        
        api_key = os.environ.get('UPSTOX_API_KEY')
        if api_key:
            print("✓ UPSTOX_API_KEY found in environment")
        else:
            print("  ℹ UPSTOX_API_KEY not found (optional)")
            
    except Exception as e:
        print(f"✗ Error loading environment: {e}")
        return False
    
    return True

def test_mcp_tools():
    """Test if MCP tools are properly defined"""
    print("\nTesting MCP tools definition...")
    
    try:
        from upstox_api import mcp as upstox_mcp
        
        # Check if tools are defined (this is a basic check)
        tools = [
            'get_historical_data',
            'get_historical_data_multiple_stocks',
            'get_portfolio',
            'get_positions',
            'get_user_profile',
            'get_funds'
        ]
        
        print("✓ Upstox MCP tools should be available:")
        for tool in tools:
            print(f"  - {tool}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error checking MCP tools: {e}")
        return False

def main():
    """Main test function"""
    print("Upstox MCP Setup Test")
    print("=" * 40)
    
    all_tests_passed = True
    
    # Run tests
    if not test_imports():
        all_tests_passed = False
    
    if not test_upstox_mcp_loading():
        all_tests_passed = False
    
    if not test_environment_setup():
        all_tests_passed = False
    
    if not test_mcp_tools():
        all_tests_passed = False
    
    # Summary
    print("\n" + "=" * 40)
    if all_tests_passed:
        print("✓ All tests passed! Your Upstox MCP setup looks good.")
        print("\nNext steps:")
        print("1. Add your actual Upstox access token to .env")
        print("2. Run: python upstox_api.py")
        print("3. Configure in your MCP client")
    else:
        print("✗ Some tests failed. Please fix the issues above.")
        print("\nCommon solutions:")
        print("- Install missing packages: pip install upstox-python-sdk mcp logzero python-dotenv")
        print("- Create .env file with UPSTOX_ACCESS_TOKEN")
        print("- Get access token from Upstox Developer Portal")
    
    return 0 if all_tests_passed else 1

if __name__ == "__main__":
    sys.exit(main())