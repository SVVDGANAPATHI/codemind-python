n=int(input())
l=list(map(int,input().split()))
s1=0
s2=0
for i in range(len(l)):
    if l[i]%2==0:
        s1+=l[i]
    else:
        s2=s2+l[i]
print(abs(s1-s2))