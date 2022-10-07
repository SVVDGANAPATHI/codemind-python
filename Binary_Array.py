n= int(input())
flag=0
l=list(map(int,input().split()))
for i in range(n):
    if l[i]!=0 and l[i]!=1:
        flag=1
        break
if flag!=0:
    print("False")
else:
    print("True")