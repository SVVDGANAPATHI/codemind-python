n=int(input())
k=n
m=n*n
c=0
while k:
    k=k//10
    c+=1
if m%10**c==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")