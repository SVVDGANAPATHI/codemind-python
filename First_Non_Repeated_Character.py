n=int(input())
for i in range(n):
    m=int(input())
    l=input()
    p=[i for i in l if i.isalnum()]
    c=0
    for i in p:
        if p.count(i)==1:
            print(i)
            c+=1
            break
    if c==0:
        print("-1")