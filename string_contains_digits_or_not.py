n=int(input())
for i in range(n):
    m=input()
    c=0
    for i in m:
        if i.isdigit():
            c+=1
    if c==0:
        print("No")
    else:
        print("Yes")