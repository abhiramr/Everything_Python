primeNumbers = []
for num in range(1, 2000):
    x = num
    count = 0
    while x > 0:
        if num %x == 0:
            count += 1
        x -= 1
    if count == 2:
        primeNumbers.append(num)
print primeNumbers
#print "Here is a list of prime numbers under 2000:"