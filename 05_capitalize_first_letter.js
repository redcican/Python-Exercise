// create a function to capitalize first letter

function capitalizeWords(str){
    let words = str.split(" ").map(word =>{
        let firstLetter = word.slice(0,1);
        let restLetter = word.slice(1);
        firstLetter = firstLetter.toUpperCase();
        return `${firstLetter}${restLetter}`;
    });

    return words.join(" ");
}


console.log(capitalizeWords("I got up early today"));
console.log(capitalizeWords("I walked straight to the beach"));
console.log("###############################")

// an effective way
function effectiveCapitalizeWords(str){
    let words = str.split(" ").map(word=>{
        return word.charAt(0).toUpperCase()+ word.slice(1);
    });
    return words.join(" ");
}
console.log(capitalizeWords("I got up early today"));
console.log(capitalizeWords("I walked straight to the beach"));
