from fastmcp import FastMCP
from z3 import *
from utils import is_valid_assert


mcp = FastMCP()

#Simple tool that uses z3-solver for symbolic execution of Python code.
@mcp.tool(name="z3_python", description="A tool that executes Z3 Python code.")
def z3_python(code: str) -> str:
    """
    Executes given Z3 Python code and returns the result.

    Args:
        code (str): Python code using z3-solver syntax.

    Returns:
        str: Output of the Z3 solver (e.g., satisfiability and model).
    """
    local_env = {"Solver": Solver, "Int": Int, "Real": Real, "Bool": Bool,
                 "sat": sat, "unsat": unsat, "unknown": unknown}
    try:
        exec(code, {}, local_env)
        if "s" in local_env and isinstance(local_env["s"], Solver):
            result = local_env["s"].check()
            if result == sat:
                model = local_env["s"].model()
                return f"SAT\nModel: {model}"
            else:
                return str(result)
        else:
            return "No solver instance named 's' found."
    except Exception as e:
        return f"Error executing Z3 code: {e}"

# Example of TiCoder's discriminative test ranking
# example prompt: Write a function to reverse the order of a string.

@mcp.tool(name="basic_ticoder")
async def basic_ticoder(prompt: str, code_list: list[str], test_list: list[str]) -> tuple[str, dict[str, Any]]:
    """
    Execute the given code snippets and run provided test assertions against them.

    Args:
        prompt (str): Description of the task.
        code_list (List[str]): Possible python code snippets that *satisfy different interpretations of the prompt*. These code snippets should capture behavior ambiguities that might not specified in the prompt.
        test_list (List[str]): tests in the form og Python `assert` statements. Make sure these tests can be executed against the codes provided, and that they cover edge cases or alternative interpretations of the prompt.

    Returns Tuple[str, Dict[str, Any]]:
            - test_for_user_response: The most discriminative test. You must ask the user about whether this test satisfies their intent.
            - discriminative_info: Dictionary containing scores and per-test breakdowns
    """


    invalid_tests = [t for t in test_list if not is_valid_assert(t)]
    if invalid_tests:
        raise ValueError(f"The following test(s) are not valid assert statements:\n" +
                         "\n".join(invalid_tests))

    discriminative_scores = []

    for test in test_list:
        pass_count = 0
        fail_count = 0

        for code in code_list:
            local_vars = {}

            try:
                exec(code, {}, local_vars)
            except Exception:
                continue  # Skip broken code for scoring

            try:
                exec(test, {}, local_vars)
                pass_count += 1
            except AssertionError:
                fail_count += 1
            except Exception:
                fail_count += 1  # Treat unexpected errors as fail for robustness

        max_val = max(pass_count, fail_count)
        min_val = min(pass_count, fail_count)
        score = 0.0 if max_val == 0 else min_val / max_val

        discriminative_scores.append({
            'test': test,
            'score': score,
            'pass_count': pass_count,
            'fail_count': fail_count
        })

    # Find test with highest discriminative score
    most_discriminative = max(discriminative_scores, key=lambda x: x['score'])
    return most_discriminative['test'], {
            'most_discriminative_test': most_discriminative['test'],
            'score': most_discriminative['score'],
            'all_scores': discriminative_scores
        }



def init_stdio_server(mcp_server):
    mcp.run()

def init_sse_server(mcp_server):
    mcp.run(transport="sse", port=9000)

def main():
    print("Starting Rise MCP Server...")
    mcp_server = mcp._mcp_server
    init_sse_server(mcp_server)


if __name__ == "__main__":
    main()



