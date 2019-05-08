// mutations


function mutation(arr){
    var firstWord = arr[0].toLowerCase();
    var secondWord = arr[1].toLowerCase();

    for (let i = 0; i < secondWord.length; i++) {
        if(firstWord.indexOf(secondWord[i]) === -1) return false;
    }

    return true;   
}


// of loog
function mutationOfLoop(arr){
    var firstWord = arr[0].toLowerCase();
    var secondWord = arr[1].toLowerCase();

    for ( var letter of secondWord) {
        if(firstWord.indexOf(letter) === -1) return false;
    }
    return true;
}

// includes method

function mutationIncludes(arr){
    var firstWord = arr[0].toLowerCase();
    var secondWord = arr[1].toLowerCase();
    
    for (var letter of secondWord) {
        if(!firstWord.includes(letter)) return false;
    }
    return true;
}

console.log(mutation(["hello", "hey"]))
console.log(mutation(["helloyy", "hey"]))
console.log("#####################")
console.log(mutationOfLoop(["hello", "hey"]))
console.log(mutationOfLoop(["helloyy", "hey"]))
console.log("#####################")
console.log(mutationIncludes(["hello", "hey"]))
console.log(mutationIncludes(["helloyy", "hey"]))