// confirm the ending of a string

function confirmEnding(str, target){
//   if(str.endsWith(target)){
//        return true;
//    }
//    return false;

// using substr() function
    if(str.substr(-target.length) === target){
        return true;
    }
    return false;
}



console.log(confirmEnding("Bastian", "n"));
console.log(confirmEnding("Bastian", "no"));
