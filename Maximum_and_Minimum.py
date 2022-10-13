n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    if l[i]==l.count(l[i]):
        l1.append(l[i])
k=list(set(l1))
k.sort()
if len(k)==0:
    print("-1")
print(min(k),max(k))
   