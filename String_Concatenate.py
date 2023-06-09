n=input()
m=input()
l=[]
for i in n:
    if i.isalnum():
        l.append(i)
for i in m:
    if i.isalnum():
        l.append(i)
print("".join(sorted(l)))