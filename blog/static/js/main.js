var user_input = $("#user-input")
var post_div = $('#replaceable-content')
var endpoint = '/ajax_search/'
var delay = 350
var scheduled_function = 0

var ajax = function (endpoint, search_parameters) {
    $.getJSON(endpoint, search_parameters)
        .done(response => {
            
                post_div.html(response['html_from_view'])
               
        })
}


user_input.on('keyup', function () {

    var search_parameters = {
        q: $(this).val() 
    }

    if (scheduled_function) {
        clearTimeout(scheduled_function)
    }

    scheduled_function = setTimeout(ajax, delay, endpoint, search_parameters)
})

