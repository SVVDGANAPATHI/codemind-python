n=input()
s=0
l="1234567890"
for i in n:
    if i in l:
        s+=int(i)
print(s)
