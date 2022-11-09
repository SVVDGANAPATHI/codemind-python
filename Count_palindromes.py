def pali(x):
    n=x
    rev=0
    while x:
        r=x%10
        rev=rev*10+r
        x=x//10
    if rev==n:
        return True
c=0
m=int(input())
l=list(map(int,input().split()))
for i in l:
    if pali(i):
        c+=1
print(c)
        