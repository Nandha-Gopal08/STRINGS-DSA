def longest_common_prefix(strs):
    first = strs[0]
    for i in range(len(first)):
        ch = first[i]
        for j in range(1,len(strs)):
            if i >= len(strs[j]) or strs[j][i] != ch:
                return first[:i]
    return first
strs = ["interview", "internet", "internal"]
print(longest_common_prefix(strs))
