def reverse_words(s):
   words = s.split()
   print(words)
   res = ""
   for i in range(len(words) - 1,-1,-1):
       res += "".join(words[i])
   return res
s = "I love DSA"
print(reverse_words(s))
