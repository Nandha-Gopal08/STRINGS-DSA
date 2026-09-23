def valid_palindrome(s):
    ch = s.replace(" ","")
    Str = ch.lower()
    left = 0
    right = len(Str) - 1
    while(left < right):
        if(Str[left] != Str[right]):
            return False

        left += 1
        right -= 1
    return True
s = "Race Car"
print(valid_palindrome(s))
