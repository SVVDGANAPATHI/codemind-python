n=int(input())
l=list(input().split())
d={}
for i in l:
    i=abs(int(i))
    d[i]=len(str(i))
z=max(d.values())
c=0
for v in d.values():
    if v==z:
        c+=1
print(c)