n=int(input())
l=list(map(int,input().split()))
s=0
l2=l.reverse()
for i in range(len(l)):
    s+=(2**i)*l[i]
print(s)    
    