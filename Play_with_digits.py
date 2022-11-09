n=int(input())
l=list(map(int,input().split()))
def sum3(x):
    s=0
    while x:
        r=x%10
        s+=r
        x=x//10
    return s
s2=0
for i in l:
    k=sum3(i)
    s2+=k
print(s2)