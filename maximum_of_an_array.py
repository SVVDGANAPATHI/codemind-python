n=int(input())
l=list(map(int,input().split()))
l.sort()
k=len(l)
print(l[k-1])