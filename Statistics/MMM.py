import math
n = int(input())
arr = input()
li = [int(x) for x in arr.split()]
mean = sum(li)/len(li)
print(mean)
li_sort = li.sort()
if len(li)%2 == 0:
    mid = int((len(li)/2))-1
    midd = int(len(li)/2)
    avg = (li[mid]+li[midd])/2
    median = avg
else:
    mid = math.floor(len(li)/2)
    median = li[mid]
print(median)
counts = []
it = 0
for i in li:
    counts.append(li.count(i))
maxx = counts.index(max(counts))
mode = li[maxx]
print(mode)

