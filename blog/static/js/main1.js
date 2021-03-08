var user_input = $("#user-input")
var user_input1 = $("#category")
var submit = $("#submit")
var post_div = $('#replaceable-content')
var endpoint = '/ajax_category/'
delay = 350
var scheduled_function = false

var ajax = function(endpoint, search_parameters) {
    $.getJSON(endpoint, search_parameters)
        .done(response => {
            
            post_div.html(response['html_from_view'])
               
        })
        .fail(function(){
            alert('Oooops');
})


submit.on('click', function () {

    var search_parameters = {
        q: $(user_input).val(),
        category : $(user_input1).val() 
    }
    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    scheduled_function = setTimeout(ajax, delay, endpoint, search_parameters)
})