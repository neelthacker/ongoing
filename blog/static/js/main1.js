var user_input = $("#user-input")
var user_input1 = $("#category")
var post_div = $('#replaceable-content')
var endpoint = '/ajax_category/'
var delay = 350
var scheduled_function = 0

var ajax = function (endpoint, search_parameters, search_parameters1) {
    $.getJSON(endpoint, search_parameters, search_parameters1)
        .done(response => {
            
                post_div.html(response['html_from_view'])
               
        })
}


user_input.on('keyup change', function () {

    var search_parameters = {
        q: $(this).val() 
    }
    var search_parameters1 = {
        q1: $(this).val() 
    }

    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    scheduled_function = setTimeout(ajax, delay, endpoint, search_parameters, search_parameters1)
})