n=input()
m=input()
l=[]
for i in n:
    l.append(i)
if m in l:
    print("True")
    print(l.index(m))
else:
    print("False")