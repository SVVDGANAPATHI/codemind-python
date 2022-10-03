n=int(input())
k=0
if n<0:
    k=1
    n=abs(n)
s=0
while n:
    r=n%10
    n=n//10
    s=s*10+r
if k==1:
    print(-s)
else:
    print(s)