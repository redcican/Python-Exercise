// caesars cipher

function rot13(str){
    var solved = "";

    for(var i=0; i < str.length; i++){
        var asciiNum = str[i].charCodeAt();
        if(asciiNum >= 65 && asciiNum<=77)
        {
            solved += String.fromCharCode(asciiNum + 13);
        }
        else if(asciiNum >=78 && asciiNum <=90)
        {
            solved += String.fromCharCode(asciiNum - 13);
        }
        else
        {
            solved += str[i];
        }
    }
    return solved;
}

//[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
console.log(rot13("A"));
console.log(rot13("SERR PBQR PNZC"))