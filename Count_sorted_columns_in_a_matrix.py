n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
k=[]
for i in range(m):
    l=[]
    for j in range(n):
        l.append(mat[j][i])
    k.append(l)
c=0
for i in k:
    if sorted(i)==i:
        c+=1
print(c)