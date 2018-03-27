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
})