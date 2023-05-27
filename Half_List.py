n=int(input())
l=list(map(int,input().split()))
a=l[len(l)//2::]
k=a[::-1]+l[:len(l)//2:]
print(*k)