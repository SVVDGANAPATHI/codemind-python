n=input().lower().split()
l=[]
for i in n:
    l.append(set(i))
a=l[0]
for i in l:
    a=a.intersection(i)
if len(a)==0:
    print("-1")
else:
    print(min(a))