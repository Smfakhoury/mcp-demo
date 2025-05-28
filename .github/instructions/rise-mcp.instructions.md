---
applyTo: '**'
---
When using the rise-mcp-server, please ensure that you follow these instructions:

### basic_ticoder tool
- When using the basic_ticoder tool you will be provided with a test case returned from the function you call. 
- You MUST ask the user about this result and whether it captures their intent, then wait for the user's answer BEFORE generating any further code.
- You must provide at least 5 codes and 10 tests
- The point of this tool is to capture ambiguities in the user's request and ask them to clarify. For this to be successful, you must provide the function with code and tests that capture the space of possible intents, to tease out this ambiguity.