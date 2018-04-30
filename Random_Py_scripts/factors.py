import sys
import gen_primes
mul=1
def factors(n,mul):
    l=gen_primes.gen_primes(n)
#    print l
    for i in range(2,n):
#        print l
        if n%i ==0:
            if i in l and mul<=n:
                print i
                mul=mul*i
            else:
                factors(i,mul)
if __name__=="__main__":
    n=int(raw_input())
    mul=1
    factors(n,mul)
