$(function() {
    $('#button').submit(function(e) {
	e.preventDefault(e);
        $.ajax({
	    url: '/',
            type: 'POST',
            success: function() {
                $('.result').show();
            }        
        });
    });
});
