n=int(input())
sum=0
m=n**2
while m:
    sum=sum +(m%10)
    m=m//10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")