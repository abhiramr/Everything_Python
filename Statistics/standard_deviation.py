import math
n = int(input())
arr = input()
intA = [int(x) for x in arr.split()]
mean = sum(intA)/len(intA)
S = 0
for i in intA:
    sqd = (i - mean)**2
    S = S + sqd
print(round(math.sqrt(S/len(intA)),1))
