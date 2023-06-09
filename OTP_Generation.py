n=input()
l=[]
for i in n:
    if int(i)%2!=0:
        l.append(str(int(i)*int(i)))
print("".join(l))