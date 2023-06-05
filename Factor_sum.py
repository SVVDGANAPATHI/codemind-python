l=list(map(int,input().split(",")))
k=[]
for i in l:
    s=0
    for j in range(1,i+1):
        if i%j==0:
            s+=j
    if s in l:
        k.append(i)
if len(k)==0:
    print("-1")
else:
    print(*sorted(k))
            