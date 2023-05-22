n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
def lent(x):
    p=abs(x)
    m=str(p)
    if len(m)==k:
        return True
    else:
        return False
for i in l:
    if lent(i):
        c+=1
print(c)
        