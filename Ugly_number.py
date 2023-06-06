n=int(input())
def p(x):
    for i in range(2,n):
        if x%i==0:
            return False
    return True
if n>0:
    l=[]
    for i in range(6,n+1):
        if p(i) and n%i==0:
            l.append(i)
            break
    if len(l)!=0:
        print("Not Ugly Number")
    else:
        print("Ugly Number")
else:
    print("Not Ugly Number")