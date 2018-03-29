$(document).ready(function() {
    for(var i = 1; i <= 151; i++){
        $.get('https://pokeapi.co/api/v2/pokemon/' + i, function(data) {
            console.log(data)
            $('div').append("<img src=" + data.sprites.front_default + ">")
        })
    }
})