n=int(input())
l=list(map(int,input().split()))
k=list(set(l))
s=0
for i in range(len(k)):
        s+=k[i]
print(s)
    