n=int(input())
l=list(map(int,input().split()))
s=0
s1=0
k=len(l)//2
for i in range(k):
    s+=l[i]
for i in range(k,len(l)):
    s1+=l[i]
print(s1-s)
