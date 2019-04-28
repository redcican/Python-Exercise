# factorialize a number and return the result

def factorialize(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result


# recursive way
def recursiveFact(num):
    return num * recursiveFact(num-1) if num >1 else 1

print(factorialize(6))
print(recursiveFact(6))