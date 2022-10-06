n=int(input())
l=list(map(int,input().split()))
l2=[]
l3=[]
l4=[]
for i in range(len(l)):
    if l[i]%2==0:
        l2.append(l[i])
    else:
        l3.append(l[i])
l4=l3+l2
for i in range(len(l3+l2)):
    print(l4[i],end=" ")