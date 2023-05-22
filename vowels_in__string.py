n=input()
f=0
l=[]
for i in n:
    if i in "aeiouAEIOU":
        if i not in l:
            l.append(i)
        f+=1
if f==0:
    print("-1")
else:
    print(*l)