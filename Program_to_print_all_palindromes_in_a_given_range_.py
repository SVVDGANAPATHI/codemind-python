def pali(x):
    rev=0
    while x:
        r=x%10
        rev=rev*10+r
        x=x//10
    return rev
n=int(input())
m=int(input())
for i in range(n,m+1):
    k=pali(i)
    if k==i:
         print(i,end=" ")