def median(li):
    li.sort()
    mid = int(len(li)/2)
    if len(li)%2 == 0:
        med = (li[mid-1] +li[mid])/2.0
    else:
        med = li[mid]
    return med


n = int(input())
arr = input()
freq = input()
intA = [int(x) for x in arr.split()]
intF = [int(x) for x in freq.split()]
li=[]
for i in range(len(intA)):
    throwaway = []
    throwaway.append(intA[i])
    throwaway = throwaway*intF[i]
    li = li +throwaway

ints = li
ints.sort()
mediI = int(len(ints)/2)
medi = median(ints)
#mediI = ints.index(medi)
f = ints[:mediI]
if len(ints)%2 == 0:
    t = ints[mediI:]
else:
    t = ints[mediI+1:]
fq = median(f)
#print(f)
#print(medi)
#print(t)
tq = median(t)
print(round(float(tq-fq), 1))
