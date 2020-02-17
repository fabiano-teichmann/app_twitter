$(document).ready(function(){
    $.ajax({
        url: "ajax_call/update_tweets",
        dataType: 'json',
        type: 'get',
        success: function(response){
            if (response['total_hashtags_updated'] > 0){
                window.location.reload()

            }

        },
    })
})