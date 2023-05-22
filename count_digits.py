n=int(input())
l=list(map(int,input().split()))
l1=[]
def lent(x):
    p=abs(x)
    m=str(p)
    return len(m)
for i in l:
    l1.append(lent(i))
print(*l1)