n=int(input())
l=list(map(int,input().split()))
f=0
for i in range(len(l)-1):
    if l[i] < l[i+1]:
        f=1
        print("no")
        break
if f==0:
    print("yes")
        