// where do I belong

function getIndexToIns(arr, num){
    arr.sort(function(a, b){
        return a-b;
    });

    for (var i=0; i<arr.length; i++){
        if (num <= arr[i]){
            return i;
        }
    }

    return arr.length;
}


console.log(getIndexToIns([40,60,5],50));
console.log(getIndexToIns([2,5,10],15))