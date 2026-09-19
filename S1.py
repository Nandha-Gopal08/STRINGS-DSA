def reverse_only_letters(s):
    s = list(s)
    left = 0
    right = len(s) - 1
    while(left < right):
        if s[left].isalpha() and s[right].isalpha():
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
        elif s[right].isalpha():
            left += 1
        else:
            right -= 1
    return "".join(s)
s = "a-bC-dEf"
print(reverse_only_letters(s))
