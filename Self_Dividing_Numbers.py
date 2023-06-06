n=int(input())
m=int(input())
def se(x):
    t=x
    l=[]
    while x:
        l.append(x%10)
        x=x//10
    for i in l:
        if i==0:
            return False
        if t%i!=0:
            return False
    return True
for i in range(n,m+1):
    if se(i):
        print(i,end=" ")
    