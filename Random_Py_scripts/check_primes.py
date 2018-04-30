import sys
def check_primes(n):
    primes_list=[]
    count=0
    for i in range(2,n):
        if n%i==0:
            count=count+1
    if count==0:
        return 0
    else:
        return 1
if __name__=="__main__":
    n=int(raw_input())
    cnt=check_primes(n)
    print cnt
   
