def regularBracketSequence1(sequence):
    stack = []
    
    for i in sequence:
        if i == '(':
            stack.append(i)
        if i == ')':
            if len(stack) == 0:
                return False
            if stack[-1] == '(':
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False
