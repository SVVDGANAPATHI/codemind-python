n=int(input())
l=list(map(int,input().split()))
m=int(input())
fc=0
for i in range(len(l)):
        if l[i]==m:
            fc+=1
if fc==0:
    print("0")
else:
    print(fc)
            
        
    