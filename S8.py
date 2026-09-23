def count_digi_letter(s):
    letter = 0
    digit = 0
    for ch in s:
        if ch.isalpha() :
            letter += 1
        if ch.isdigit():
            digit += 1
    return letter,digit
s = "abc123def45"
print(count_digi_letter(s)) 
