n = int(input())
for i in range(n):
    v = 0
    c = 0
    t = input()
    for j in t:
        if j in "aeiou":
            v = v + 1
        else:
            c = c + 1
    print(v, c, sep="  ")