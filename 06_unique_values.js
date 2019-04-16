// return true only if all values are unique, otherwise false
// using Array, object, string method lastIndexOf()
// no Set data structure

function unique(str){

    for (let i = 0; i < str.length; i++) {
        if(str.lastIndexOf(str[i])!==i){
            return false;
        };
    }
    return true;

    // object case
    // let values = {};
    // for (let letter of str) {
    //     if(values[letter]){
    //         return false;
    //     }
    //     values[letter] = "exists";
    // }
    // return true;


    // str case
    // let values = []
    // for (let letter of str) {
    //     if(values.indexOf(letter)!==-1){
    //         return false;
    //     }
    //     values.push(letter);
    // }
    // return true;
}

// true
console.log(unique("abced"));
// false
console.log(unique("abacdefb"));