n=int(input())
p=64+n
o=n+1
for i in range(n):
    for j in range(o-1):
        print(chr(p),end=" ")
    p-=1
    o=o-1
    print('')