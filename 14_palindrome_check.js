// check a given string is a palindrome or not
// A palindrome is a word or sentence that’s spelled the same way both forward and backward, 
// ignoring punctuation, case, and spacing.
// You’ll need to remove all non-alphanumeric characters (punctuation, spaces and symbols) 
// and turn everything lower case in order to check for palindromes.

function palindrome(str){
    var reg = /[\W_]/g;
    var smallStr = str.toLowerCase().replace(reg, "");
    var reversed = smallStr.split("").reverse().join("");

    if(reversed === smallStr){
        return true;
    }
    return false;
}

// true
console.log(palindrome("eye"));
// true
console.log(palindrome("_eye"));
// true
console.log(palindrome("race car"));
// false
console.log(palindrome("not a palindrome"));
// true
console.log(palindrome("A man, a plan, a canal, Panama"));
// true
console.log(palindrome("never odd or even"));
// false
console.log(palindrome("nope"));
// false
console.log(palindrome("almostomla"));
// true
console.log(palindrome("My age is 0, 0 si ega ym."));
// true
console.log(palindrome("0_0(:/-\:)0-0"));