n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(len(l)):
    s=1
    for j in range(len(l)):
        if i!=j:
            s*=l[j]
    k.append(s)
print(*k)