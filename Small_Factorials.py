n=int(input())
for i in range(n):
    m=int(input())
    def fa(x):
        s=1
        while x>0:
            s*=x
            x=x-1
        return s
    print(fa(m))