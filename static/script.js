$(function() {
    $('#button').click(function() {
        $.ajax({
	    url: '/#',
            type: 'POST',
            success: function(response) {
                $('.result').show();
            }        
        });
    });
});
