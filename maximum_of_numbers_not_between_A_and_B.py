n=int(input())
l=list(map(int,input().split()))
k,j=map(int,input().split())
l3=[]
for i in range(len(l)):
    if l[i]<k or l[i]>j:
         l3.append(l[i])

if len(l3)==0:
    print("-1")
else:
    print(max(l3))