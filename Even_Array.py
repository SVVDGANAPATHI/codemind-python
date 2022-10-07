n=int(input())
l=list(map(int,input().split()))
flag=0
for i in range(len(l)):
    if l[i]%2!=0 or l[i]==0:
        flag+=1
if flag==0:
    print("True")
else:
    print("False")
        
        