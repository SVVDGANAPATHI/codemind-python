n=list(input().split())
k=[]
def re(x):
    return x[::-1]
for i in n:
    k.append(re(i))
print(*k)
