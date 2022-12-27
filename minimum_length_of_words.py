l=list(input().split())
d={}
for i in l:
    d[i]=len(i)
z=min(d.values())
print(z)