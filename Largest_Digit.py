m=int(input())
list1=[]
while m:
    r=m%10
    list1.append(r)
    m=m//10
print(max(list1))
    
