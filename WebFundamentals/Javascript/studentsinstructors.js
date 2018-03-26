function printNames(obj){
    console.log("Students")
    for(var i=0;i<obj.Students.length;i++){
        var firstName = obj.Students[i].first_name 
        var lastName = obj.Students[i].last_name
        var length = (firstName + lastName).length
        console.log((i+1) + ' - ' + firstName + ' ' + lastName + ' - ' + length )
    }
    console.log("Instructors")
    for(var i=0;i<obj.Instructors.length;i++){
        var firstName = obj.Instructors[i].first_name 
        var lastName = obj.Instructors[i].last_name
        var length = (firstName + lastName).length
        console.log((i+1) + ' - ' + firstName + ' ' + lastName + ' - ' + length )
    }
}