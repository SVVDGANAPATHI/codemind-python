n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l1=[]
f=0
for i in range(len(l)):
    if l[i]<a or l[i]>b:
        l1.append(l[i])
        f+=1
if f==0:
    print("-1")
print(min(l1))