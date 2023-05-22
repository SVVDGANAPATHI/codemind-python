z=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=[i for i in a if i not in b]
l=l+[i for i in b if i not in a]
print(*l)