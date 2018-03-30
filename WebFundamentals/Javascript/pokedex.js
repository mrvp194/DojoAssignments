$(document).ready(function() {
    var info = {}
    
    function getPokemon(i) {
        $('#pokemon').append("<img id=" + i + " src=''>")
        $.get('https://pokeapi.co/api/v2/pokemon/' + i, function(data) {
            
            info[i] = data
            document.getElementById(i).src = data.sprites.front_default 
        })
    }

    for(var i = 1; i <= 151; i++){
        getPokemon(i)
    }

    $('#pokemon').on('click', 'img', function(){
        var num = event.target.id
        var poke = info[num]
        var h1 = '<h1>' + poke.name + '</h1>'
        var img = "<img src=" + poke.sprites.front_default + ">"
        var type = '<ul>'
        for(var x = 0; x < poke.types.length; x++){
            type += '<li>' + poke.types[x].type.name + '</li>'
        }
        type += '</ul>'
        var heightHeader = '<h3>Height</h3>'
        var height = '<p>' + poke.height + '</p>'
        var weightHeader = '<h3>Weight</h3>'
        var weight = '<p>' + poke.weight + '</p>'
        
        $('#pokedex').html(h1 + img + type + heightHeader + height + weightHeader + weight)
    })
})