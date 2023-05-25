n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
l=[]
k=[]
for i in range(m):
    s=0
    for j in range(n):
        s+=mat[j][i]
    l.append(s)
for i in mat:
    k.append(sum(i))
p=max(l)
i=max(k)
print(max(p,i))
        
    