def valid_parentheses(s):
    stack = []
    pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
    }
    for ch in s:
        if ch  in "({[":
            stack.append(ch)
        else:
            if not stack:
                return False
            if pairs[ch] != stack[-1]:
                return False
            stack.pop()
    return len(stack) == 0
s = "({[]{})"
print(valid_parentheses(s))
