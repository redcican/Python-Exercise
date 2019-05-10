# Seek and Destroy

def destroy(*args):
    args = list(args)
    source = args[0]
    target = args[1:]
    result = []
   
    for num in source:
        if not target.__contains__(num):
            result.append(num)
    return result


# Using list  comprehensions

def destroyList(*args):
    args = list(args)

    result = [x for x in args[0] if x not in args[1:]]
    return result

# using Set() operation

def destroySet(*args):
    args = list(args)
    result = list(filter(lambda x: x not in set(args[1:]), args[0]))
    return result


print(destroy([1,2,3,1,2,3],2,3))
print(destroy([1,2,3,3,3,3,4,5,],1,3))
print('\n')
print(destroyList([1,2,3,1,2,3],2,3))
print(destroyList([1,2,3,3,3,3,4,5,],1,3))
print('\n')
print(destroySet([1,2,3,1,2,3],2,3))
print(destroySet([1,2,3,3,3,3,4,5,],1,3))