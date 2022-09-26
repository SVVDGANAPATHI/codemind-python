import math
n=int(input())
sum=0
while n:
        r=n%10
        n=n/10
        sum=sum+r
def add(x):
    sum2=0
    while x:
        r1=x%10
        x=x/10
        sum2=sum2+r1
        return(sum2)
k= add(sum)
print(math.floor(k))

