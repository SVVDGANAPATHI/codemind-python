m=int(input())
l1=list(map(int,input().split()))
count=0
for i in range(1,len(l1)-1):
    if l1[i]%2!=0 and l1[i-1]%2==0 and l1[i+1]%2==0:
        count+=1
print(count)