def prime(y):
    fc=0
    for i in range(1,y+1):
        if y%i==0:
            fc+=1
    return fc
    
n=int(input()) 
x=n
k=prime(n)
if k!=2:
    print("not prime")
elif k==2:
    s=0
    while n:
        r=n%10
        s=s*10+r
        n=n//10
    l=prime(s)
    if l!=2:
            print("prime but not a circular prime")
    elif l==2:
            print("circular prime")
            
    
  


