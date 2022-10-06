n=int(input())
l1=list(map(int,input().split()))
for i in range(n-1,-1,-1):
    if l1[i]%2!=0:
        print(l1[i])
        break