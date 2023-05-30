n=input()
l=[]
k=[]
for i in n:
    if i in "aeiou" and i not in l:
        l.append(i)
    elif i in "AEIOU" and i not in k:
        k.append(i)
if len(l)==5:
    print("True")
elif len(k)==5:
    print("True")
else:
    print("False")