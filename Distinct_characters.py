n=input().lower()
n=n.replace(" ",'')
l=[]
d={}
for i in n:
    if i not in d:
        d[i]=1
        l.append(i)
    else:
        d[i]+=1
p=[k for k,v in d.items() if v==1]
print("".join(sorted(p)))