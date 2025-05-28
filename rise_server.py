from mcp.server.fastmcp import FastMCP
import argparse
from utils.server_utils import create_starlette_app
import uvicorn
import os

mcp = FastMCP()

@mcp.tool()
def dummy_rise_tool(a:int, b:int) -> str:
    """
    A dummy rise tool that does nothing.

    returns:
        str: A message indicating that the dummy rise tool was executed successfully.
    """
    print("This is a dummy rise tool. It does nothing.")
    return "Dummy rise tool executed successfully."

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



