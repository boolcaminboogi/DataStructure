def checkBrackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{', '[', '('):
#        if ch in '{[(':
            stack.push(ch)
        elif ch in ('}', ']', ')'):
            if stack.isEmpty() :
                return False
            else :
                left = stack.pop()
                if (ch == "}" and left != "{") or \
                   (ch == "]" and left != "[") or \
                   (ch == ")" and left != "(") :
                    return False

    return stack.isEmpty()

# {{{{{{{(((
# '
# "
# #
# '''