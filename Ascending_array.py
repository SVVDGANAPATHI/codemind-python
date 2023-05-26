n=int(input())
l=list(map(int,input().split()))
k=0
for i in range(len(l)-1):
    if l[i] < l[i+1]:
        k+=1
if len(l)-1==k:
    print("yes")
else:
    print("no")