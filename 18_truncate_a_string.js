// truncate a string

function truncateString(str, num){
    if (num >= str.length) return str;
    else if (num <= 3) return str.slice(0, num) + "...";
    return str.slice(0, num-3) + "...";
}


console.log(truncateString("A-tisket a tasket A green and yellow basket", 11));
console.log(truncateString("tommy goes to work.", 3));
console.log(truncateString("A-tisket a tasket A green and yellow basket","A-tisket a tasket A green and yellow basket".length + 2));
