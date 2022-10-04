a,b=map(int,input().split())
l1=list()
l2=list()
l3=list()
i=1
for i in range(100):
    l1.append(a*i)
    l2.append(b*i)
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            l3.append(l1[i])
print(l3[1])
    
    