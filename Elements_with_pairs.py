n=int(input())
l=list(map(int,input().split()))
if n%2!=0:
    l.append(0)
    for i in range(len(l)):
        print(l[i],end=" ")
else:
    for i in l:
        print(i,end=" ")