import math
def p(x):
    if x==1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
n=int(input())
f=0
for i in range(1,n):
    if n%i==0 and p(i) and p(n//i):
        f=1
        print(i,n//i)
        break
if f==0:
    print("-1")
    