n=int(input())
for i in range(n):
    m,p=map(int,input().split())
    l=list(map(int,input().split()))
    o=list(map(int,input().split()))
    u=l+o
    print(*sorted(u))