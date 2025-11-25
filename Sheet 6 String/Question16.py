a = input(" ")
b = input(" ")
c = 0
i = 0

while i < len(a) - len(b) + 1:
    if a[i:i+len(b)] == b:
        c = c + 1
    i = i + 1
print(c)
