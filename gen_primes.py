import sys
def gen_primes(n):
    primes_list=[]
    count=0
    for i in range(2,n):
        for j in range(2,i):
            if i%j ==0:
                count=count+1
        if count == 0:
            primes_list.append(i)
        else:
            count=0
    return primes_list
if __name__=="__main__":
    n=int(raw_input())
    primes_list=gen_primes(n)
    print primes_list
   
