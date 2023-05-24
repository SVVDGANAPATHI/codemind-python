p=int(input())
l=list(map(int,input().split()))
c=c1=0
for i in l:
    if i%2==0:
        c+=1
    else:
        c1+=1
print(c,c1)