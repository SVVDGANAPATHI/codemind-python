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
t=p.symmetric_difference(o)
t=list(t)
t.sort()
print(len(t))