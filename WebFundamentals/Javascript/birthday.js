function birthday(num){
    var sad = num +" days until my birthday.  Such a long time... :("
    var happy = num + " DAYS"
    if(num >= 30){
        console.log(num +" days until my birthday.  Such a long time... :(")
    }else if(num < 30 && num > 5){
        console.log(num + " days until my birthday.  Getting close!")
    }else if(num <= 5 && num > 1){
        console.log(num + " DAYS UNTIL MY BIRTHDAY!!!")
    }else if(num === 1){
        console.log("1 DAY UNTIL MY BIRTHDAY!!!")
    }else{
        console.log("HAPPY BIRTHDAY!!!!!!!")
    }
}