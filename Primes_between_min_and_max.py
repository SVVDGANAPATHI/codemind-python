n=int(input())
l=list(map(int,input().split()))
m=max(l)
k=min(l)
if l.index(m)<l.index(k):
    x,y=l.index(m),l.index(k)
else:
    x,y=l.index(k),l.index(m)
c=0
def prime(x):
    fc=0
    for i in range(1,x+1):
        if x%i==0:
            fc+=1
    if fc==2:
        return True
    else:
        return False
for i in range(x,y+1):
    if prime(l[i]):
        c+=1
print(c)
    