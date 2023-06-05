n=int(input())
l=list(map(int,input().split()))
k=int(input())
if k not in l:
    print("-1 -1")
else:
    for i in range(len(l)):
        if l[i]==k:
            print(i,end=" ")
            break
    for i in range(len(l)-1,-1,-1):
        if l[i]==k:
            print(i,end=" ")
            break
    
