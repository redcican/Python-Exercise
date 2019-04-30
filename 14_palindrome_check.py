# check a given string is a palindrome or not
# A palindrome is a word or sentence that’s spelled the same way both forward and backward, 
# ignoring punctuation, case, and spacing.
# You’ll need to remove all non-alphanumeric characters (punctuation, spaces and symbols) 
# and turn everything lower case in order to check for palindromes.

import re

def palindrome(string):
    pattern = r'[\W_]'
    smallString = re.sub(pattern, "", string.lower())
    reversedString = ''.join(list(reversed(smallString)))

    if reversedString == smallString:
        return True
    return False



print(palindrome("eye"))
print(palindrome("_eye"))
print(palindrome("race car"))
print(palindrome("not a palindrome"))
print(palindrome("A man, a plan, a canal, Panama"))
print(palindrome("never odd or even"))
print(palindrome("nope"))
print(palindrome("almostomla"))
print(palindrome("My age is 0, 0 si ega ym."))
print(palindrome("0_0(:/-\:)0-0"))

