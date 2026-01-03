import json
from typing import Any

def print_dict(d: dict, indent: int = 0, prefix: str = "") -> None:
    """
    Recursively prints all keys/values in a nested dictionary (or list).

    Parameters
    ----------
    d : dict | list
        The data structure to walk through.
    indent : int, optional
        Current indentation level – used internally for recursion.
    prefix : str, optional
        A string that is printed before the key.  Useful when you want to
        differentiate between top‑level keys and nested ones (e.g. `"messages[0].content"`).

    Notes
    -----
    * If a value is itself a dictionary or list it will be recursed into.
    * For lists we show the index in brackets (`[0]`, `[1]` …).
    * Strings are printed raw; everything else is converted to JSON for readability.
    """
    if isinstance(d, dict):
        for key, val in d.items():
            # Build a readable path
            path = f"{prefix}.{key}" if prefix else key

            if isinstance(val, (dict, list)):
                print(f"{'  '*indent}{path}:")
                print_dict(val, indent + 1, path)
            else:
                # Show the value – pretty‑print JSON for non‑strings
                display = (
                    val
                    if isinstance(val, str)
                    else json.dumps(val, ensure_ascii=False, default=str)
                )
                print(f"{'  '*indent}{path}: {display}")

    elif isinstance(d, list):
        for i, item in enumerate(d):
            path = f"{prefix}[{i}]" if prefix else f"[{i}]"
            if isinstance(item, (dict, list)):
                print(f"{'  '*indent}{path}:")
                print_dict(item, indent + 1, path)
            else:
                display = (
                    item
                    if isinstance(item, str)
                    else json.dumps(item, ensure_ascii=False, default=str)
                )
                print(f"{'  '*indent}{path}: {display}")

    else:   # base case – not a dict/list (shouldn't happen in this usage)
        path = prefix or "<root>"
        display = (
            d
            if isinstance(d, str)
            else json.dumps(d, ensure_ascii=False, default=str)
        )
        print(f"{'  '*indent}{path}: {display}")


from pprint import pformat

def pretty_print(obj, indent=0):
    """Recursively pretty print nested message structures."""
    spacing = "  " * indent

    if isinstance(obj, dict):
        print(f"{spacing}{{")
        for k, v in obj.items():
            print(f"{spacing}  {k!r}:")
            pretty_print(v, indent + 2)
        print(f"{spacing}}}")

    elif isinstance(obj, list):
        print(f"{spacing}[")
        for i, item in enumerate(obj):
            print(f"{spacing}  [{i}]")
            pretty_print(item, indent + 2)
        print(f"{spacing}]")

    elif hasattr(obj, "__dict__"):  # For custom objects like AIMessage, ToolMessage, etc.
        print(f"{spacing}{obj.__class__.__name__}(")
        for k, v in vars(obj).items():
            print(f"{spacing}  {k}:")
            pretty_print(v, indent + 2)
        print(f"{spacing})")

    else:
        # For simple types (str, int, None, etc.)
        pretty_value = pformat(obj, indent=2, width=80, compact=True)
        print(f"{spacing}{pretty_value}")
