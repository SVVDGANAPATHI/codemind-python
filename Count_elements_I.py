n,m=map(int,input().split())
s=set(map(int,input().split()))
p=set(map(int,input().split()))
z=s&p
print(len(z))