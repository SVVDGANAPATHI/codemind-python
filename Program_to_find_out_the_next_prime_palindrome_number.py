import math
def pr(x):
    if x==1:
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True
def pali(x):
    s=str(x)
    if s==s[::-1]:
        return True
    else:
        return False
n=int(input())
for i in range(n+1,100000):
    if pr(i) and pali(i):
        print(i)
        break