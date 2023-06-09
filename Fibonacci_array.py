n=int(input())
l=list(map(int,input().split()))
f=0
for i in range(1,len(l)-1):
    if l[i+1]-l[i-1]!=l[i]:
        f+=1
        break
if f==0 and l[n-3]+l[n-2]==l[n-1]:
    print("yes")
else:
    print("no")