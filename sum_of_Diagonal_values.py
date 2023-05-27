n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
s=0
for i in range(n):
    for j in range(m):
        if i==j or i==m-j-1:
            s+=mat[i][j]
print(s)