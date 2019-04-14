# create a function to capitalize first letter

def capitalizeWords(str):
    result = ' '.join(word[0].upper() + word[1:] for word in str.split())
    return result


print(capitalizeWords("I got up early today"))
print(capitalizeWords("I walked straight to the beach"))
print("#################################")

# an effective way
def effectiveCapitalizeWords(str):
    return str.title()


print(effectiveCapitalizeWords("I got up early today"))
print(effectiveCapitalizeWords("I walked straight to the beach"))