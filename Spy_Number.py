n=int(input())
sum=0
fact=1
while n>0:
    sum=sum+(n%10)
    fact=fact*(n%10)
    n=n//10
if fact==sum:
    print("Spy Number")
else:
    print("Not Spy Number")
    