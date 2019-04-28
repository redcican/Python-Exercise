// factorialize a number and return the result

function factorialize(num){
    var result = 1;

    for (var i=1; i<=num; i++){
        result *= i;
    }
    return result;
}

// recursive way
function recursiveFact(num){
    if(num > 1){
        return num * recursiveFact(num - 1);
    }
    else{
        return 1;
    }
}

console.log(factorialize(6));
console.log(recursiveFact(6));