n=input()
l=[]
for i in range(2,int(n)):
    if str(i)==str(i)[::-1]:
        l.append(int(i))
for i in range(int(n)+1,int(n)**2):
    if str(i)==str(i)[::-1]:
        l.append(int(i))
        break
ma=l[-1]
mi=l[-2]
if ma-int(n)==int(n)-mi:
    print(mi,ma)
elif ma-int(n) < int(n)-mi:
    print(ma)
else:
    print(mi)