n=input()
f=0
for i in range(len(n)):
    if n.count(n[i])==1:
        print(i)
        f=1
        break
if f==0:
    print("-1")
else:
    pass