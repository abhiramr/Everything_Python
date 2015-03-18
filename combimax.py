# PEP-8 Compliant
import itertools


def permutations_plus(k, r):
    k.sort()
    li = itertools.combinations(k, r)
    max_min = []
    for k in li:
        max_min.append(int(k[-1])-int(k[0]))  # (max(k)-min(k)))
    val=min(max_min)
    return val
if __name__ == '__main__':
    tc = int(input())
    r = int(input())
    arr = []
    for i in range(tc):
        arr.append(int(input()))
    #  arr=set(arr)
    ans=permutations_plus(arr, r)
    print "Minimum difference = ", ans
