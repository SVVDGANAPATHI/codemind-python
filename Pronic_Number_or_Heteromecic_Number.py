m=int(input())
count=0
for i in range(m):
    if i*(i+1)==m:
        count+=1
if count!=0:
    print("YES")
else:
    print("NO")