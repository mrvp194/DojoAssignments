function fancyArray(arr, symbol = "->", reversed = false){
    if(reversed === true){
        arr = arr.reverse()
    }
    for(var i=0; i<arr.length; i++){
        console.log(i + " " + symbol + " " + arr[i])
    }
}