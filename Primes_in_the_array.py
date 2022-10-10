n=int(input())
l=list(map(int,input().split()))
def prime(x):
    if x==1 and x==0:
        return False
    else:
        fc=0
        for i in range(1,x+1):
            if x%i==0:
                fc+=1
        if fc==2:
            return True
c=0
for i in range(len(l)):
    if prime(l[i]):
        c+=1
print(c)