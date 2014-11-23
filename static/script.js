$(function() {
    $('#button').click(function(){
      $.ajax({
	url: '/',
        type: 'POST',
	data: $('#input').serialize(),
        success: function(response) {
          $('.result').html(response);
	  $("#input").val('');
        }
      });
    });
});
