n=int(input())
l=list(map(int,input().split()))
s1=0
for i in range(len(l)):
    s1+=l[i]
    m=s1/n
print("{:.2f}".format(m))