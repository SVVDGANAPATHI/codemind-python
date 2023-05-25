def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
f=0
n=int(input())
l=[]
for i in range(1,n):
    for j in range(2,n):
        if prime(i) and prime(j):
            if i*j==n:
                f=1
                l.append(i)
                l.append(j)
                break
if f==0:
    print("-1")
else:
    print(*set(l))
