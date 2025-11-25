vowels = 'aeiouAEIOU'
s = 'aeiOUz'
s = s+s
for i in s:
    if i.isupper():
        s = s.replace(i, "")
    elif i in vowels:
        s = s.replace(i, "#")

print(s)