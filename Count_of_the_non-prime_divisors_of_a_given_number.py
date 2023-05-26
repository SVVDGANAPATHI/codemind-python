import math
n=int(input())
def pr(x):
    if x==1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True
c=0
for i in range(1,n+1):
    if pr(i)==False and n%i==0:
        c+=1
print(c)
        
        