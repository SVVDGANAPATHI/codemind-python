n=list(input().split())
c=0
k=['a','e','i','o','u']
for i in n:
    if i[0].lower() in k and i[-1].lower() not in k:
        c+=1
print(c)
    