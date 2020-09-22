function myFunc(x,y,back){
    return back(x+y)
}

function closFunc(val){
    return Math.pow(val,2)
}

console.log(myFunc(1,2,closFunc))
