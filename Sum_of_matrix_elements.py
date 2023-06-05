m=int(input())
n=int(input())
mat=[list(map(int,input().split())) for i in range(m)]
s=0
for i in mat:
    s+=sum(i)
print(s)    