n=int(input())
l=["0","1"]
a=0
b=1
for i in range(2,100):
    c=a+b
    l.append(c)
    a=b
    b=c
f=0
for i in l:
    if i==n:
        f=1
        break
if f==0:
    print("False")
else:
    print("True")

