n=input()
l=n.lower()
l=l.replace(" ","")
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
c=0
for k,v in d.items():
    if v==1:
        c+=1
print(c)