def count_vow(s):
    count = 0
    for ch in "aeiouAEIOU":
        count += s.count(ch)
    return count
s = "programming"
print(count_vow(s))
