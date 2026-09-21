def String_compression(s):
    res = ""
    count = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            res = res + s[i] + str(count)
            count = 1
    res = res + s[-1] + str(count)
    return res
            
        
        
        
s = "aaabbccccd"
print(String_compression(s))
