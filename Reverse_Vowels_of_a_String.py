n=input()
x=list(n)
l=[]
for i in range(len(x)):
    if x[i] in "aeiouAEIOU":
        l.append(x[i])
        x[i]="*"
l.reverse()
j=0
for i in range(len(x)):
    if x[i]=="*":
        x[i]=l[j]
        j+=1
print("".join(x))
