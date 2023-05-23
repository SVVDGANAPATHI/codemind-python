n=input()
l=['a','e','i','o','u','A','E','I','O','U']
c=0
for i in n:
    if i in l:
        c+=1
if c==0:
    print("0")
else:
    print(c)