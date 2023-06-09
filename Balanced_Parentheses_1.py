l=[]
n=input()
f=0
for i in n:
    if i in"({[":
        l.append(i)
    elif i==")" and l[-1]=='(':
            l.pop()
    elif i==']'and l[-1]=='[':
            l.pop()
    elif i=="}" and l[-1]=='{':
            l.pop()
if len(l)==0 and n[0] not in ")}]":
    print("True")
else:
    print("False")