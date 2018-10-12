const user1 = "https://s3-ap-southeast-1.amazonaws.com/cuora/person_icon.png";
const bot = "https://s3-ap-southeast-1.amazonaws.com/cuora/cuoraavatar.svg";
const prodURL = "";
const devURL = 'http://127.0.0.1:5000';

var serverUrl = devURL;


function insertText(who, text){

    var control = '';

    if (who == "me"){
      control = '<li>' +
      '<div class="left-chat">' +
      '<img src="' + user1 + '">' +
      '<p>'+ text +'</p>' + 
      '</div>' +
      '</li>';                    
    }
    else{
      control = '<li>' +
      '<div class="right-chat">' +
      '<img src="' + bot + '">' +
      '<p>' + text + '</p>' + 
      '</div>' +
      '</li>';  
    }

    $(".chat-input").append(control);
    // Always call scrollTop on the div element, and either the UL or DIV element can be used to get scrollHeight
    $('.chat-section').scrollTop($('.chat-section')[0].scrollHeight);

}


$(".chattextbox").on('keyup', function (e) {
	if (e.which == 13){
	    var text = $(this).val();
      var invalid = /\s\s\s/g;
	    if (text != ""){
	        insertText("me", text);              
	        $(this).val('');
          $.post( serverUrl + "/lex", {'inputText': text })
          .done(function(response){
            insertText("bot", response);
        })
	    }
	}
});