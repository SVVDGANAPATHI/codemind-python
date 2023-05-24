n=list(input().split())
def pali(x):
    m=str(x).lower()
    if m==m[::-1]:
        return True
    else:
        return False
c=0
for i in n:
    if pali(i):
        c+=1
print(c)
    