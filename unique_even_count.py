n=int(input())
l=list(map(int,input().split()))
k=list(set(l))
c=0
for i in range(len(k)):
    if k[i]%2==0:
        c+=1
print(c)
    