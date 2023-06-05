n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
c=0
for i in mat:
    if sorted(i)==i or sorted(i,reverse=True)==i:
        c+=1
print(c)
        
    