A = input("")
B = int(input(" "))
c = chr(B)  
if c in A:
    print(A.index(c))   
else:
    print(-1)            
