// Remove all falsy values from an array.
// Falsy vlaue in JS are 'false', 'null', 0, '', undefined
// and 'NaN'

function bounce(arr){
    var truthies = [];

    for (var element of arr)
    {
        if(element)
            {
                truthies.push(element);
            }
    }

    return truthies;
}


// filter function

function bounceFilter(arr){
    return arr.filter(function(item){
        return item;
    })
}

console.log(bounce([7, "ate", "", false, 0]));
console.log(bounceFilter([7, "ate", "", false, 0]));
console.log(bounceFilter(["", 0, false, undefined, NaN]));
