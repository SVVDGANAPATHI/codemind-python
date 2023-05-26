import math
n=int(input())
m=int(input())
def prime(x):
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True
for i in range((n+m)+1,1000):
    if prime(i):
        print(i-(n+m))
        break
    