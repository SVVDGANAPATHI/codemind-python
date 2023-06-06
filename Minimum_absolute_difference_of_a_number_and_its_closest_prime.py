n=int(input())
def p(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
l=[]
for i in range(2,n):
    if p(i):
        l.append(i)
for i in range(n+1,n**2):
    if p(i):
        l.append(i)
        break
if p(n):
    print("0")
elif l[-1]-n < n-l[-2]:
    print(abs(l[-1]-n))
else:
    print(abs(l[-2]-n))