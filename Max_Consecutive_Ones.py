n=int(input())
l=list(input().split())
m="".join(l)
m=m.split("0")
o=0
for i in m:
    if len(i)>o:
        o=len(i)
print(o)
    