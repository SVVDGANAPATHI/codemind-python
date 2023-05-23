l=list(input().split())
def cou(x):
    l1=['a','e','i','o','u']
    c=0
    for i in x:
        if i.lower() in l1:
            c+=1
    return c
k=[]
for i in l:
    k.append(cou(i))
print(max(k))
    
            