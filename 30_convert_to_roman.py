# Convert a number to roman number

def convertToRoman(num):
    romanToNum = {
        'M' : 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }

    roman = ""

    for key,value in romanToNum.items():
        while num >= value:
            roman += key
            num -= value

    return roman


print(convertToRoman(3))
print(convertToRoman(8))
print(convertToRoman(27))