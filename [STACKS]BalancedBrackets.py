def balancedBrackets(string):
    stack = []
    dict = {"{":"}", "[":"]", "(":")"}
    for char in string:
        if char not in "{}[]()":
            continue
        elif not stack or dict.get(stack[-1]) != char:
            stack.append(char)
        else:
            stack.pop()
    return len(stack) == 0
        
