def rot_str(s1,s2):
    if(len(s1) == len(s2)):
        if(s2 in (s1+s1)):
            return True
    return False
s1 = "waterbottle"
s2 = "erbottlewat"
print(rot_str(s1,s2))
