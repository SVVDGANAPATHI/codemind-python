import math
n=int(input())
def p(x):
    if x==1:
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True
if n<0:
    print("Not Ugly Number")
else:
    f=0
    for i in range(6,n+1):
        if p(i)==True and n%i==0:
            f=1
            print("Not Ugly Number")
            break
    if f==0:
        print("Ugly Number")
    