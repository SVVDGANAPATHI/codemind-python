n=int(input())
for i in range(n):
    c=0
    m=input()
    for i in m:
        if i in ['0','1','2','3','4','5','6','7','8','9']:
            c+=1
    if c==len(m):
            print("True")
    else:
            print("False")
        