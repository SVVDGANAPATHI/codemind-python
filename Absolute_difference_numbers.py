n,m=input().split()
p=n[:int(m):]
o=n[-1:-(int(m)+1):-1]
o=o[::-1]
print(abs(int(o)-int(p)))