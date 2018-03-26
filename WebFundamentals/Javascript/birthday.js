function countdown(num){
    while (num >= 30){
        console.log(num +" days until my birthday.  Such a long time... :(")
        num--
    }
    while (num < 30 && num > 5){
        console.log(num + " days until my birthday.  Getting close!")
        num--
    }
    while (num <=5 && num > 1){
        console.log(num + " DAYS UNTIL MY BIRTHDAY!!!")
        num--
    }
    while (num === 1){
        console.log("1 DAY UNTIL MY BIRTHDAY!!!")
        num--
    }
    while (num === 0){
        console.log("HAPPY BIRTHDAY!!!!!!!")
        break
    }
}