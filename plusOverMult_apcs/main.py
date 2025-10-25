def main():
    expr = input()
    
    # print(hasPlus(expr))
    while not isSolved(expr):
        while (plus_index := hasOp(expr, "+")) and (plus_index is not None):
            expr = calculate(plus_index, expr)
            # print(expr)
        
        while (f_count := has_f(expr)) and (f_count is not None):
            expr = resolve_f(expr, f_count)
            # print(expr)
            while (plus_index := hasOp(expr, "+")) and (plus_index is not None):
                expr = calculate(plus_index, expr)
                # print(expr)
        
        while (mult_index := hasOp(expr, "*")) and (mult_index is not None):
                expr = calculate(mult_index, expr)
                # print(expr)
        
    print(expr)

def f(*args):
    return max(args) - min(args)

def calculate(op_index, expr):
    # calculate + and *
    ESCAPE_CHARACTERS = ("*", "+", "f", "(", ")", ",")
    
    lower_bound, upper_bound = 0, 0
    for i, val in enumerate(reversed(expr[:op_index])):
        lower_bound = i
        if val in ESCAPE_CHARACTERS:
            lower_bound -= 1
            break
        
    for j, val in enumerate(expr[op_index + 1:]):
        upper_bound = j
        if val in ESCAPE_CHARACTERS:
            upper_bound -= 1
            break
    # print(f"{lower_bound} {upper_bound}")
    toBeProcessed = expr[op_index - lower_bound - 1:op_index + upper_bound + 1 + 1]
    res = eval(toBeProcessed)
    # print(toBeProcessed)
    return expr.replace(toBeProcessed, str(res), 1)

def resolve_f(expr, f_count):
    # print(eval("f(f(f(0)))"))
    expr = expr.replace("f", "t", f_count - 1)
    
    f_index = expr.index("f")
    upper_bound = 0
    
    for i, val in enumerate(expr[f_index:], f_index):
        upper_bound = i
        if val == ")":
            upper_bound -= 1
            break
    toBeProccessed = expr[f_index:upper_bound + 1 + 1]
    # print(toBeProccessed, upper_bound)
    res = eval(toBeProccessed)
    # print(f"{toBeProccessed}={res}")
    
    # print(expr.replace(toBeProccessed, str(res)).replace("d", "f"))
    
    return expr.replace(toBeProccessed, str(res)).replace("t", "f")

def hasOp(expr, op_type):
    # ignores f()
    for i, char in enumerate(expr):
        if (char == op_type) and (expr[i - 1] != ")") and (expr[i + 1] != "f"):
            return i
    else:
        return None

def has_f(expr):
    f_count = len(expr) - len(expr.replace("f", ""))
    
    return f_count if f_count != 0 else None
 
def isSolved(res):
    try:
        int(res)
        return True
    except ValueError:
        return False
    
if __name__ == "__main__":
    main()
