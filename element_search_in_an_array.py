n=int(input())
l=list(map(int,input().split()))
m=int(input())
flag=0
for i in range(len(l)):
    if l[i]==m:
        flag=1
if flag==0:
    print("False")
else:
    print("True")