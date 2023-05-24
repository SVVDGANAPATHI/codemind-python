n=input()
l=[32]+[i for i in range(65,91)]
k=[i for i in range(97,123)]
c=0
for i in n:
    if ord(i) not in l and ord(i) not in k:
        c+=1
print(c)