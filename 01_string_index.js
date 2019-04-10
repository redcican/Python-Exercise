// return the first index of serach string in the source string

function findFirstMatch(searchString, sourceString)
{
    let length = searchString.length;
    for (let index = 0; index< sourceString.length; index++) {
        let possibleMatch = (
            sourceString.substr(index, length));
        if (possibleMatch == searchString){
            return index;
        }
        }
    return -1;
}

let testStr = "abcdefghiyes";
let searchStr = "yes";
console.log(findFirstMatch(searchStr, testStr));