n=int(input())
l=list(map(int,input().split()))
k,j=map(int,input().split())
l2=[]
for i in range(len(l)):
    if l[i]<k or l[i]>j:
        l2.append(l[i])
s=0
for i in range(len(l2)):
    s+=l2[i]
print(s)   
    
