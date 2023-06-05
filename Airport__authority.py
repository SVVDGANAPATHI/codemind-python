n=int(input())
k=[]
for i in range(n):
    k.append(int(input()))
t=int(input())
s=0
for i in k:
    if i <= t:
        s+=1
    else:
        s+=2*1
print(s)