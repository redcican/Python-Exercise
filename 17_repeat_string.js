// repeat a string num times

function repeatStringNumTimes(str, num){
       if (num < 0) return "";   
       return str.repeat(num);
}


// without using built-in function
function repeatStringForLoop(str, num){
    if (num < 0) return "";
    final = "";
    for(var i=0; i <num; i++){
        final += str;
    }
    return final;
}

// using recuision method
function repeatStringRecuision(str, num){
    if(num < 0) return "";

    if(num ===1) return str;
    return str + repeatStringRecuision(str, num - 1);
}

console.log(repeatStringNumTimes("abc", 3));
console.log(repeatStringNumTimes("abc", 4));
console.log(repeatStringRecuision("a bc", 5));