// Seek and Destroy

function destroyer(arr){

    var args = Array.from(arguments);
    args.splice(0, 1);
    var target = args;
    var result = [];

    for (var num of arr) {
        if(target.indexOf(num) === -1){
            result.push(num);
        }
    }

    return result;
}

// filter function

function destroyerFilter(arr){

    var args = Array.from(arguments);
    args.splice(0, 1);
    var target = args;

    return arr.filter(function(num){
        return target.indexOf(num) === -1;
    })
}

console.log(destroyer([1,2,3,1,2,3],2,3));
console.log(destroyer([1,2,3,3,3,3,4,5,],1,3));
console.log(destroyerFilter([1,2,3,1,2,3],2,3));
console.log(destroyerFilter([1,2,3,3,3,3,4,5,],1,3))