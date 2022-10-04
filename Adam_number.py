m=int(input())
k=m*m
s=0
while m:
    r=m%10
    s=s*10+r
    m=m//10
s2=s**2
s3=0
while s2:
    r1=s2%10
    s3=s3*10+r1
    s2=s2//10
if s3==k:
    print("True")
else:
    print("False")