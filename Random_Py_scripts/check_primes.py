"""Script to return if a number is prime"""

def check_primes(num_to_check):
    """
    Function to check if a number is prime
    """
    count = 0
    for i in range(2, num_to_check):
        if num_to_check%i == 0:
            count = count+1
    if count == 0:
        return 1
    return 0

if __name__ == "__main__":
    NUM = int(input())
    CNT = check_primes(NUM)
    print("Prime" if CNT == 1 else "Not Prime")
