n=int(input())
count=0
for i in range(n):
    if i*i==n:
        print("True")
        count+=1
if count==0:
    print("False")