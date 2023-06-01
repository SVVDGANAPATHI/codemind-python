n=input().lower().split()
m=input().lower().split()
l=[]
for i in m:
    if i in n and not i in l:
        l.append(i)
print(*l)
        