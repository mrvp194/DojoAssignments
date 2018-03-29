$(document).ready(function() {
    $('form').submit(function() {
        // console.log(this)
        var place = this[0].value
        $.get('http://api.openweathermap.org/data/2.5/weather?q=' + place + '&&appid=9be6ab9cfecc32d9d817a9f1170cd046', function(data) {
            console.log(data)
            var valNum = data.main.temp
            var temp = ((valNum-273.15)*1.8)+32
            var name = data.name
            $('div').html("<h1>" + name + "</h1><h3>" + Math.round(temp) + "</h3>")
        })
        return false
    })
})