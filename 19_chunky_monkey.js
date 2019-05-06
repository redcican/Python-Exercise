// chunky monkey split a array into two sub arrays

function chunkyMonkey(arr, size){
    var groups = [];
    while (arr.length > 0){
        groups.push(arr.slice(0, size));
        arr = arr.slice(size);
    }

    return groups;
}

// function splice

function chunkyMonkeySplice(arr, size){
    var groups = [];
    while(arr.length > 0){
        groups.push(arr.splice(0, size));
    }
    return groups;
}

console.log(chunkyMonkey(["a","b","c","d"],2));
console.log(chunkyMonkey(["d","e", "f","g","h"],4));
console.log(chunkyMonkeySplice(["a","b","c","d"],2));
console.log(chunkyMonkeySplice(["d","e", "f","g","h"],4));