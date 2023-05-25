n,m=map(int,input().split())
m=[list(map(int,input().split())) for i in range(n)]
s=0
for i in m:
    s=s+sum(i)
print(s)