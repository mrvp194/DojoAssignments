function tellTime(hour, minute, period){
    var string;
    var string2;
    if(minute < 30){
        string = "just after"
    }else if(minute > 30) {
        string = "almost"
    }else {
        string = "half past"
    }
    if(period === "AM"){
        string2 = "morning"
    }else {
        string2 = "evening"
    }
    console.log("It's " + string + " " + hour + " in the " + string2)
}
tellTime(8, 30, "AM")