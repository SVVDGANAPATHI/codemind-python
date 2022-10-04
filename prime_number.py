m=int(input())
flag=0
for i in range(1,100):
    if i==m or i==1:
        continue
    if m%i==0:
        flag=1
if flag!=0:
    print("not a prime")
else:
    print("prime")