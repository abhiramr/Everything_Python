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
ints = [int(x) for x in arr.split()]
mediI = int(len(ints)/2)
medi = median(ints)
#mediI = ints.index(medi)
f = ints[:mediI]
if len(ints)%2 == 0:
    t = ints[mediI:]
else:
    t = ints[mediI+1:]
fq = median(f)
print(f)
print(medi)
print(t)
tq = median(t)
print(int(fq))
print(int(medi))
print(int(tq))
