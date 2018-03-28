$(document).ready(function() {
    var first;
    var last;
    var desc;
    $('form').submit(function() {
        // var form = $(this).serialize()
        // console.log(form)
        first = this[0].value
        last = this[1].value
        desc = this[2].value
        $('#info').append("<div class='card'><h1>" + first + " " + last + "</h1><p>Click for Description</p></div>")
        return false
    })
    $('body').on('click', '.card', function() {
        // console.log($(this).html())
        if($(this).html() === "<p>" + desc + "</p>") {
            $(this).html("<h1>" + first + " " + last + "</h1><p>Click for Description</p>")
        } else {
            $(this).html("<p>" + desc + "</p>")
        }
        
    })
})