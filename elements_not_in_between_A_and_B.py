n=int(input())
l=list(map(int,input().split()))
k,j=map(int,input().split())
l2=[]
for i in range(len(l)):
    if l[i]<k or l[i]>j:
        l2.append(l[i])

for i in range(len(l2)):
    print(l2[i],end=" ")
if len(l2)==0:
    print("-1")
    
   
    