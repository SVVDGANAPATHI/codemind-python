n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
s=0
for i in range(n):
    for j in range(m):
        if i==0 or j==0 or i==n-1 or j==m-1:
            s+=mat[i][j]
print(s)
        
    