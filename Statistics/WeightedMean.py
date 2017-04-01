n = int(input())
arr = input()
weights = input()
li = [int(x) for x in arr.split()]
li_w = [int(x) for x in weights.split()]
sums=0
for i in range(len(li)):
    sums = sums + li[i]*li_w[i]

w_avg = sums/sum(li_w)
print(round(w_avg, 1))
