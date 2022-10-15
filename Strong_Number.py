n=int(input())
t=n

def fact(x):
    p=1
    if x==1:
        return 1
    for i in range(1,x+1):
        p*=i
    return p
s=0
while n:
    r=n%10
    d=fact(r)
    s+=d
    n=n//10
if t==s:
    print("The number",t,"is a strong number")
else:
    print("The number",t,"is not a strong number")
    