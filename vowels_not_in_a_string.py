n=input()
l=[]
k="aeiou"
p=[]
for i in n:
    if i in "aeiou" and i not in l:
        l.append(i)
if len(l)==5:
    print("0")
else:
    for i in k:
        if i not in l:
            p.append(i)
    print(*p)
        