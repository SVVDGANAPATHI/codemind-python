n=input().lower().split()
m=input().lower().split()
l=[]
k=[]
for i in n:
    for j in i: 
       if j not in l:
          l.append(j)
for i in m:
    for j in i: 
       if j not in k:
          k.append(j)
p=set(l)
o=set(k)
t=p.intersection(o)
if len(t)==0:
    print("-1")
else:
    t=list(t)
    t.sort()
    print("".join(t))
