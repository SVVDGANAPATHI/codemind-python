def prime(x):
    fc=0
    for i in range(1,x+1):
        if x%i==0 or x==1:
            fc+=1
    return fc
n=int(input())
l=[]
l2=[]
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
for i in range(len(l)):
    k=prime(l[i])
    if k!=2:
        l2.append(l[i])
print(len(l2))
        