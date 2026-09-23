def char_freq(s):
    seen = set()
    res = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            c = s.count(ch)
            res.append(f"{ch}->{c}")
    return res
s = "banana"
print(char_freq(s))

"""Output:
b → 1
a → 3
n → 2"""
