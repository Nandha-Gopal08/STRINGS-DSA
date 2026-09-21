def dupli_char(s):
    res = ""
    for i in range(len(s)):
        if s[i] not in res:
           
            res += s[i]
    return  res
s = "mississippi"
print(dupli_char(s))


