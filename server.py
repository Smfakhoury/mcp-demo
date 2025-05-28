import subprocess
from mcp.server.fastmcp import FastMCP
import argparse
from utils.server_utils import create_starlette_app
import uvicorn
import os

mcp = FastMCP()

@mcp.tool(name="add", description="A tool that adds two numbers.")
def add(a: int, b: int) -> int:
    """
    Adds two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def init_stdio_server(mcp_server):
    mcp.run()

def init_sse_server(mcp_server):
    mcp.run(transport="sse")

def main():
    print("Starting Rise MCP Server...")
    mcp_server = mcp._mcp_server
    init_sse_server(mcp_server)


if __name__ == "__main__":
    main()



