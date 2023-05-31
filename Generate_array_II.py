n=int(input())
l=list(map(int,input().split()))
n=l[0::2]
k=l[1::2]
for i in range(len(n)):
    p=k[i]
    while p:
        print(n[i],end=" ")
        p=p-1


    