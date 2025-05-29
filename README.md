# MCP Server Examples

This repository contains examples of how to develop and use MCP servers with Visual Studio Code Copilot. There is also some sample code for using features like prompts, and resources, which are supported by other MCP clients (like Claude Desktop) but not yet a part of VS Code. 

### Pre-requisites
- Install the latest version of [Visual Studio Code Insiders](https://code.visualstudio.com/insiders/)
- Access to Copilot
- Python 3.11 or later 


### Clone this repository
```bash
git clone https://github.com/Smfakhoury/mcp-demo.git
cd mcp-demo
```
### Install dependencies
```
python3.11 -m venv .venv
source .venv/bin/activate  
pip install -r requirements.txt
```

### Run the server
```bash
python server.py
```
### Connect in vscode
1. Open a copilot chat window 
2. Click on the tools icon
3. '+ add more tools
4. 'add MCP server' -> HTTP
5. Enter the server url 
6. Add to settings

### To use the server
1. Open a copilot chat window
2. Reference the tool you want to use using '#' 
3. Make sure to include the rise-mcp.instructions file as a reference

