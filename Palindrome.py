def reverse(num):
        rev=0
        while num:
                d=num%10
                num=num//10
                rev=rev*10+d
                
        return rev
num=int(input())
if num==reverse(num):
    print("True")
else:
    print("False")
