from __future__ import print_function
import itertools
import sys

gl=[]
def permute(items,length):
  #  length = len(items)
    def inner(ix=[]):
        do_yield = len(ix) == length - 1
        for i in range(0, length):
            if i in ix: #avoid duplicates
                continue
            if do_yield:
                yield tuple([items[y] for y in ix + [i]])
            else:
                for p in inner(ix + [i]):
                    yield p
    return inner()

def chef(n,k,l):
    l2=[s for s in range(1,k+1)]
    l2=l2*n
    l3=[]
    for i in itertools.permute(l2,n):
        l3.append(i)
    l4=list(set(l3))
    l4.sort()
    gl.append(l4[l-1])

if __name__=="__main__":
    tc=int(raw_input("Enter tc:"))
    for i in range(tc):
        inp=raw_input() 
        mynums = [int(i) for i in inp.split()]
        chef(mynums[0],mynums[1],mynums[2])
    for i,j in enumerate(gl):
        print(*j,sep=' ')
