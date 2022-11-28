n=input()
x=0
y=0
for i in n:
    if i=='z':
        x+=1
    if i=='o':
        y+=1
if 2*x==y:
    print("Yes")
else:
    print("No")