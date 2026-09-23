def check_pre_suf(s,pre,suf):
    return s.startswith(pre),s.endswith(suf)
s = "programming"
pre = "pro"
suf = "ing"
print(check_pre_suf(s,pre,suf))
