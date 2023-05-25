n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
e=0
o=0
for i in range(n):
    for j in range(m):
        if mat[i][j]%2==0:
            e+=mat[i][j]
        else:
            o+=mat[i][j]
print(e,o)