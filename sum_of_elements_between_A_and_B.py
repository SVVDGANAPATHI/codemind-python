n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in range(len(l)):
    if a<=l[i]<=b:
        s+=l[i]
print(s)