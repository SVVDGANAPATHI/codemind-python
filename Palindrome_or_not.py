n=list(input().split())
def pali(x):
    m=str(x).lower()
    if m==m[::-1]:
        return True
    else:
        return False
for i in n:
    if pali(i):
        print("True")
    else:
        print("False")
    