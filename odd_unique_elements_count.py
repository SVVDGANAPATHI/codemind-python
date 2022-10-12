n=int(input())
l=list(map(int,input().split()))
k=list(set(l))
s=0
for i in range(len(k)):
    if k[i]%2!=0:
        s+=1
print(s)
    