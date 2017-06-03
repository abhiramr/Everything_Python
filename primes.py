def prime(n):
    for i in range(2,n/2):
        if n%i ==0:
            return 1;
    return 0;
    
    
n=2000
count=0
for i in range (2,n):
    st = prime(i)
    if st == 0:
        print i