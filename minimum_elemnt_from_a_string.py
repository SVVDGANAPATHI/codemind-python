n=list(input().split())
k=n[-1]
l=[i for i in k]
def order(n):
    return ord(n)
l.sort(key=order)
if l[0].lower() in l:
    print(l[0].lower())
else:
    print(l[0])
    
    