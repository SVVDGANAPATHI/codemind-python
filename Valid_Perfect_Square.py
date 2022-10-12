def square(x):
    for i in range(1,x+1):
        if i*i==x:
            return True
n=int(input())
for i in range(1,n+1):
    m=int(input())
    if square(m):
        print("True")
    else:
        print("False")