def evaluate(expr: str) -> int:
    """
    Evaluates an expression string based on the problem's custom rules:
    1. Innermost f() functions are resolved first.
    2. All additions are performed.
    3. All multiplications are performed last.

    Args:
        expr: The expression string to evaluate.

    Returns:
        The integer result of the evaluation.
    """
    # Base case: if the expression is already a single number, return it.
    # This is crucial for the recursion to terminate.
    try:
        return int(expr)
    except ValueError:
        # If it's not a simple integer, it's a complex expression that needs processing.
        pass

    # Step 1: Resolve all f() functions from the inside out.
    # The loop continues as long as there are functions to process.
    while 'f(' in expr:
        # Use rfind() to locate the start of the rightmost 'f(', which guarantees
        # it is an innermost function with no other 'f' calls inside its arguments.
        start = expr.rfind('f(')

        # Find the matching closing parenthesis for this function call.
        paren_balance = 0
        end = -1
        for i in range(start + 2, len(expr)):
            if expr[i] == '(':
                paren_balance += 1
            elif expr[i] == ')':
                if paren_balance == 0:
                    end = i
                    break
                paren_balance -= 1
        
        # Extract the arguments string from within the parentheses.
        args_str = expr[start + 2 : end]

        # Split the arguments string by top-level commas, respecting nested parentheses.
        args_list = []
        if args_str:
            paren_balance = 0
            last_split_idx = 0
            for i, char in enumerate(args_str):
                if char == '(': paren_balance += 1
                elif char == ')': paren_balance -= 1
                elif char == ',' and paren_balance == 0:
                    args_list.append(args_str[last_split_idx:i])
                    last_split_idx = i + 1
            args_list.append(args_str[last_split_idx:])
        
        # Recursively call evaluate() on each argument to resolve them to numbers.
        evaluated_args = [evaluate(arg) for arg in args_list]
        
        # Apply the f() function logic: max(args) - min(args).
        f_result = 0 if not evaluated_args else max(evaluated_args) - min(evaluated_args)
            
        # Replace the entire f(...) substring with its numeric result.
        expr = f"{expr[:start]}{f_result}{expr[end + 1:]}"

    # Step 2: Once all f() are resolved, evaluate the flat expression.
    # The expression now only contains numbers, '+', and '*'.
    # Per the "add first, then multiply" rule, we first split by '*'...
    product = 1
    for term in expr.split('*'):
        # ...then for each resulting term, we sum its parts split by '+'.
        product *= sum(map(int, term.split('+')))
        
    return product


if __name__ == "__main__":
    # Read the expression from standard input.
    expression_to_solve = input()
    # Evaluate and print the final result.
    print(evaluate(expression_to_solve))
