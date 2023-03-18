def sortStack(stack):
    newStack = []
    while stack:
        top = stack.pop()
        newStack.append(top)
    while newStack:
        newTop = newStack.pop()
        while stack and stack[-1] > newTop:
            newStack.append(stack.pop())
        stack.append(newTop)
    return stack
            
