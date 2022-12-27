l=list(input().split())
d={}
for i in l:
    d[i]=len(i)
z=max(d.values())
print(z)