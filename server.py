from fastmcp import FastMCP


# FastMCP handles all the complex protocol details and server management
mcp = FastMCP()

#Sample tool, added to the mcp instance, name and description used by LLM

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
    mcp.run(transport="sse", port=2223)

def main():
    print("Starting Rise MCP Server...")
    mcp_server = mcp._mcp_server
    init_sse_server(mcp_server)


if __name__ == "__main__":
    main()



