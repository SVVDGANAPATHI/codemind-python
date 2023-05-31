n=int(input())
l=[0, 1, 2, 3, 5, 8,13,21, 34, 55, 89, 144]
mini=0
maxi=0
for i in range(len(l)-1):
    if l[i] <=n and n<=l[i+1]:
        mini=l[i]
        maxi=l[i+1]
        break
if n-mini < maxi-n:
    print(mini)
elif n-mini == maxi-n:
    print(mini,maxi)
else:
    print(maxi)
