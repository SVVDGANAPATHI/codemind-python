n=int(input())
def reverse(x):
    rev=0
    while x:
        r=x%10
        rev=rev*10+r
        x=x//10
    return rev
l=list(map(int,input().split()))
l1=[]
for i in l:
    l1.append(reverse(i))
for i in l1:
    print(i,end=" ")
