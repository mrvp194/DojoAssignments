$(document).ready(function() {
    $('#first button').click(function() {
        $('div').css("background", "red")
    })
    $('#second button').click(function() {
        $('div').append("<p>Here's some stuff!!!</p>")
    })
    $('#third button').click(function() {
        $('div').hide()
    })
    $('#show').click(function() {
        $('div').show()
    })
    $('#fifth').click(function() {
        $('div').slideDown('slow')
    })
    $('#fourth button').click(function() {
        $('div').slideUp('slow')
    })
    $('#sixth button').click(function() {
        $('div').fadeOut('slow')
    })
    $('#seventh').click(function() {
        $('div').fadeIn('slow')
    })
})