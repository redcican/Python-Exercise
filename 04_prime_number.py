# Check whether a number is a prime number or not
# prime number = can only divide evenly by itself of one
import math

def isPrime(num):
    if num < 2:
        return False
    root = math.ceil(math.sqrt(num))

    for i in range(2, root+1):
        if num % i == 0:
            return f"{num} is not a prime number"
    
    return f"{num} is a prime number"


print(isPrime(8))
print(isPrime(11))
print(isPrime(121))
print(isPrime(127))

    