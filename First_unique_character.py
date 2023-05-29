n=input()
d={}
for i in n:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
f=0
for k,v in d.items():
    if v==1:
        print(k)
        f=1
        break
if f==0:
    print("-1")