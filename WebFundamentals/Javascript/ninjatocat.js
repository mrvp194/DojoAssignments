$(document).ready(function(){
    $('img').click(function(){
        var alt = this.dataset.altSrc
        this.dataset.altSrc = this.src
        this.src = alt
    })
})