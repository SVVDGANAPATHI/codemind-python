n=input()
d={}
for i in n:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
l=[i for i in d.values()]
l.sort()
k=set(l)
if len(k)==1:
    print("-1")
else:
    l=list(k)
    m=l[-2]
    for k,v in d.items():
        if v==m:
            print(k)
            break