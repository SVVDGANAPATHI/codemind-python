n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(len(l)):
    if l[i]==l.count(l[i]):
        if l[i] not in l1:
            l1.append(l[i])
if len(l1)==0:
    print("-1")
for i in l1:
    print(i,end=" ")
   