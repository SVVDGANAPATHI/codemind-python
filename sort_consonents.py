t=list(input().split())
def pal(n):
    x=list(n)
    l=[]
    for i in range(len(x)):
        if x[i] not in "aeiouAEIOU":
            l.append(x[i])
            x[i]="*"
    l.sort()
    j=0
    for i in range(len(x)):
        if x[i]=="*":
            x[i]=l[j]
            j+=1
    return "".join(x)
p=[]
for i in t:
    p.append(pal(i))
print(*p)
    
    