n=int(input())
l=list(map(int,input().split()))
k=[]
l1=[]
l2=[]
if n%2!=0:
    for i in range(n//2):
        k.append(l[i])
    for i in range(n//2,n):
        l1.append(l[i])
    l2.append(l1[0])
    l1.reverse()
    for i in range(len(k)):
        print(k[i],l1[i],end=" ")
    print(l2[0],0)
else:
    for i in range(n//2):
        k.append(l[i])
    for i in range(n//2,n):
        l1.append(l[i])
    l1.reverse()
    for i in range(len(k)):
        print(k[i],l1[i],end=" ")