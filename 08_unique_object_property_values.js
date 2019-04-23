// dynamic filter the unique value of an array

let products = [
    {
        title: "Iphone 8",
        company: "apple"
    },
    {
        title: "Galaxy",
        company: "samsung"
    },
    {
        title: "Iphone 7",
        company: "apple"
    },
    {
        title: "Iphone Xs",
        company: "apple"
    },
    {
        title: "HTC Phone",
        company: "htc"
    }
]

function getUnique(arr){
    let tempArr = arr.map(item => item.company);
    return [...new Set(tempArr)];
}

function effecientGetUnique(arr){
    return [
        ...arr.reduce((acc, curr) =>{
            acc.add(curr.company);
            return acc;
        }, new Set())
    ];
}

console.log(getUnique(products));
console.log(effecientGetUnique(products));