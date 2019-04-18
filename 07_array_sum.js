// check if all the numbers summed up 
// are equal to a largest number that 
// we have in an array

function ArraySum(arr){
    let tempArr = arr.sort((a,b)=>{
        return a -b;
    });
    let largest = tempArr.pop();

    let number = 0;
    tempArr.forEach(item => {
        (number += item);
    });
    return largest === number;
}


// returns true 1+2++4+6=13
console.log(ArraySum([1,2,4,6,13]));
// returns false 1+2+4+22=29 != 34
console.log(ArraySum([1,2,4,34,22]));