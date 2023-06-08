n=int(input())
l=list(map(int,input().split()))
k=[i for i in l if i%2==0]
m=[i for i in l if i%2!=0]
for i in range(n):
    if i < len(m):
        print(m[i],end=" ")
    if i < len(k):
        print(k[i],end=" ")
if n%2!=0:
        print('0')
        