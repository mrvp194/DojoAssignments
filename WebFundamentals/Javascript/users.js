$(document).ready(function() {
    $('form').submit(function() {
        // console.log($(this))
        // var form = $(this).serialize()
        // console.log(form)
        var first = this[0].value
        var last = this[1].value
        var email = this[2].value
        var phone = this[3].value
        $('table').append('<tr><td>' + first + '</td><td>' + last + '</td><td>' + email + '</td><td>' + phone + '</td></tr>')
        return false
    })
})