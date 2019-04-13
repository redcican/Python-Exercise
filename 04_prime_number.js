// Check whether a number is a prime number or not
// prime number = can only divide evenly by itself or one

function isPrime(num){
    if(num < 2){
        return false;
    }

    let root = Math.ceil(Math.sqrt(num));

    for (let i = 2; i <= root; i++) {
        if(num % i == 0){
            return `${num} is not a prime number`;
        }        
    }
    return `${num} is a prime number`;
}
// false
console.log(isPrime(8));
// true
console.log(isPrime(11));
// false
console.log(isPrime(121));
// true
console.log(isPrime(127));
