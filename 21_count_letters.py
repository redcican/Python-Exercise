# Count repeating letters
# string will not contain numbers or submols only letters


def countLetters(string):
    x = {i: string.count(i) for i in string}
    letters = []
    
    for k, v in x.items():
        value = f'{v}{k}'
        letters.append(value)
    return ''.join(letters)


print(countLetters('ffffeeerttttooooo'))



