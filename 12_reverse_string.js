// reverse a string

function reverseString(str){
    var strArr = str.split("");
    var reverseStrArray = strArr.reverse();
    var reversedString = reverseStrArray.join("");
    return reversedString;

    //return str.split("").reverse().join("");
    
    // another method
    // var final = "";
    // for (var i=str.length-1; i>=0; i--){
    //    final += str[i];
    //}
    // return final;
}

console.log(reverseString("hello"));