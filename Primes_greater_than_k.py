def prime(x):
    fc=0
    if x==1:
        return False
    for i in range(1,x+1):
        if x%i==0:
            fc+=1
    if fc==2:
        return True
n=int(input())
l=list(map(int,input().split()))
m=int(input())
c=0
for i in l:
    if i>=m:
       if prime(i):
           c+=1
print(c)

        
        