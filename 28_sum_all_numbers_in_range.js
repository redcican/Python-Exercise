// Sum all numbers in a range

function sumAll(arr){
    var start = Math.min(arr[0], arr[1]);
    var end = Math.max(arr[0], arr[1]);

    var total = 0;
    for (var i = start; i <= end; i++){
        total += i;
    }

    return total;
}


console.log(sumAll([1,4]));
console.log(sumAll([5,1]));
console.log(sumAll([100,0]))
