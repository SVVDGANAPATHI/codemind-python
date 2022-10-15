n=int(input())
if n<0:
    print("False")
def pali(x):
    q=x
    if x<0:
        return False
    rev=0
    while x:
        r=x%10
        rev=rev*10+r
        x=x//10
    if rev==q:
        return True
    else:
        return False
for i in range(n):
    m=int(input())
    if pali(m):
        print("True")
    else:
        print("False")
       