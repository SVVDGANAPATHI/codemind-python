n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(len(l)):
    s+=l[i]
a=s//n
c=0
for i in range(len(l)):
    if l[i]>=a:
        c+=1
print(c)
