import ast


def is_valid_assert(test: str) -> bool:
        try:
            node = ast.parse(test)
            return (
                isinstance(node, ast.Module) and
                len(node.body) == 1 and
                isinstance(node.body[0], ast.Assert)
            )
        except SyntaxError:
            return False
