n=list(input().split())
def rev(x):
    return x[::-1]
for i in range(len(n)-1,-1,-1):
    print(rev(n[i]),end=" ")