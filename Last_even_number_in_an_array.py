n=int(input())
l=list(map(int,input().split()))
k=len(l)
l2=[]
for i in range(len(l)):
    if l[i]%2==0:
        l2.append(l[i])
print(max(l2))
    