from itertools import permutations
n=input()
p=permutations(n)
for i in p:
    print("".join(i))