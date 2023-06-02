import math
n1=int(input())
n2=int(input())
def p(x):
    if x==1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
n=n1+n2
for i in range(n+1,n**2):
    if p(i):
        print(i-n)
        break