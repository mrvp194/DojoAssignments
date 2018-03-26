function printRange(start, end, interval = 1){
    if(end === undefined){
        end = start
        start = 0
    }
    for(var i = start; i < end; i=i+interval){

        console.log(i)
    }
}
