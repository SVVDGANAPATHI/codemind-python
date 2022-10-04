n=int(input())
l1=list()
while n>0:
    r=n%10
    n=n//10
    l1.append(r)
l1.reverse()
for i in range(len(l1)):
    if l1[i]==6:
        l1[i]=9
        break
for i in range(len(l1)):
    print(l1[i],end="")