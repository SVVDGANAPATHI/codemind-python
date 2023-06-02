import math
n=int(input())
m=int(input())
def p(x):
    if x==1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
c=0
for i in range(n,m+1):
    if p(i):
        c+=1
print(c)