s,t,b=map(int,input().split())
l=['K','B']
l2=[round((2*s*t*b*512)/1024)]
l3=l2+l
for i in range(len(l3)):
    print(l3[i],end="")