n=int(input())
flag=0
for i in range(1,n+1):
    if i*i==n:
        flag=1
        print("True")
        break
if flag==0:
    print("False")