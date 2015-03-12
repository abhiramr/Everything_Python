import itertools
def permy(k,r):
    k.sort()
    li=itertools.combinations(k,r)
    mami=[]
    for k in li:
        mami.append(int(k[-1])-int(k[0])) #(max(k)-min(k)))
    val=min(mami)
    return val
if __name__ == '__main__':
    tc=int(input())
    r=int(input())
    arr=[]
    for i in range(tc):
        arr.append(int(input()))
    #arr=set(arr)
    ans=permy(arr,r)
    print "Minimum difference = ",ans
