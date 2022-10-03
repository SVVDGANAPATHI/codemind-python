def self(num):
    temp=num
    while temp:
        r=temp%10
        temp=temp//10
        if r==0 or num%r!=0:
            return False
    return True
n=int(input())
m=int(input())
for i in range(n,m+1):
    if self(i):
        print(i,end=" ")
        