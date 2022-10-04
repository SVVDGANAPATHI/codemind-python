n=int(input())
x=n
s=0
l1=list()
l2=list()
while n:
    r=n%10
    n=n//10
    l1.append(r)
l1.reverse()
for i in range(len(l1)):
    l2.append(l1[i]**(i+1))
s1=0
for i in range(len(l2)):
    s1=s1+l2[i]
if s1==x:
    print("True")
else:
    print("False")

    
    