n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
f=0
for i in range(len(l)):
    if a<=l[i]<=b:
        print(l[i],end=' ')
        f+=1
if f==0:
    print("-1")
