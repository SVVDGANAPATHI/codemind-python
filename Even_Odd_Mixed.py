n=int(input())
ec=0
oc=0
while n:
    r=n%10
    if n%2==0:
        ec+=1
    elif n%2!=0:
        oc+=1
    n=n//10
if oc==0:
    print("Even")
elif ec==0:
    print("Odd")
else:
    print("Mixed")