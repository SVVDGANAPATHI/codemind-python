n=int(input())
l=list(map(int,input().split()))
l1=[]
def lent(x):
    p=abs(x)
    m=str(p)
    l1.append(len(m))
def le(x):
    p=abs(x)
    k=str(p)
    if len(k)==m:
        return x
    else:
        return False
for i in l:
    lent(i)
m=max(l1)
for i in l:
    if le(i):
        print(i,end=" ")
    
    