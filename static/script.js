$(function() {
    $('#button').click(function(){
      var data = {text: $('#input').val()};
      console.log(data);
      $.ajax({
	url: '/',
        type: 'POST',
	contentType: 'application/json; charset=utf-8',
	dataType: 'json',
	data: JSON.stringify(data),
        success: function(data) {
          alert(data);
        }
      });
    });
});
