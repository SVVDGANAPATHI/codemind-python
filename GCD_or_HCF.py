a,b=map(int,input().split())
l1=list()
l2=list()
l3=list()
for i in range(1,a+1):
    if a%i==0:
        l1.append(i)
for j in range(1,b+1):
    if b%j==0:
        l2.append(j)
for i in range(len(l1)):
    for j in range(len (l2)):
        if l1[i]==l2[j]:
            l3.append(l1[i])
l3.sort()
k=len(l3)
print(l3[(k-1)])
        