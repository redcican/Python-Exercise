// Find the longest word in a sentence

function longestWord(sentence){
    let words = sentence.split(" ");
    let longestWord = "";

    for(let word of words){
        if(word.length > longestWord.length){
            longestWord = word;
        }
    }
    return longestWord;
}

console.log(longestWord("I woke up up early today."));
console.log(longestWord("I went straight to the beach."));