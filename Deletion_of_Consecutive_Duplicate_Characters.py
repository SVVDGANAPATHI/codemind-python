t=int(input())
for i in range(t):
    n=input()
    c=0
    for i in range(1,len(n)):
        if n[i-1] == n[i]:
            c+=1
    print(c)