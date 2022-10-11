def happy(n):
    res=0
    while n:
      r=n%10
      res+=r*r
      n=n//10
    return res  
n=int(input())
result=n
while result!=1 and result!=4:
    result=happy(result)
if result==1:
    print("True")
elif result==4:
    print("False")

    