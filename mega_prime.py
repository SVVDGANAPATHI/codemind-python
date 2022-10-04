import math
m=int(input())
def isprime(m):
    sq=int(math.sqrt(m))
    for i in range(2,sq+1):
        if m%i==0:
            return False
    return True
if isprime(m):
    while m:
        d=m%10
        m=m//10
        if d==1 or d==4 or d==6 or d==9:
            print("Not Mega Prime")
            break
    else:
        print("Mega Prime")

else:
    print("Not Mega Prime")


