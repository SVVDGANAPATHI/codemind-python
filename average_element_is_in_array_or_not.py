n=int(input())
l=list(map(int,input().split()))
s1=0
for i in range(len(l)):
    s1+=l[i]
    m=s1//n
flag=0
for i in range(len(l)):
    if l[i]==m:
        flag=1
if flag==0:
    print("False")
else:
    print("True")