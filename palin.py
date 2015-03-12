#!/usr/bin/py
import itertools
def palin_or_not(strA):
    if strA == strA[::-1]:
        print(strA)
        return 1
    else:
        return 0
if __name__=='__main__':
    strA=raw_input()
    if len(strA) == len(set(strA)):
        print("NO")
    else:
        for i in itertools.permutations(strA,len(strA)):
            k=palin_or_not(''.join(i))
            if k == 1:
           # print(''.join(i))
                print("YES")
                break
        if k == 0:
            print("NO") 
