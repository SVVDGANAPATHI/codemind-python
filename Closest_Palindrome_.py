n=int(input())
l=[]
for i in range(n):
    i=str(i)
    if i==i[::-1]:
        l.append(int(i))
for i in range(n+1,n**2):
    i=str(i)
    if i==i[::-1]:
        l.append(int(i))
        break
ma=l[-1]
mi=l[-2]
if ma-n == n-mi:
    print(mi,ma)
elif ma-n < n-mi:
    print(ma)
else:
    print(mi)