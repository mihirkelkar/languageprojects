//Project Euler problem 3
var pal_numbers = []
for (var i = 100; i <= 999; i++) {
	for(var j = i; j <= 999; j++){
		var newString = i * j;
                if(check_palindrome(newString.toString())){
		  var palindrome = newString;
		}
	}
}

debug("Largest palindrome is " + palindrome);

function check_palindrome(newString){
	if(newString.charAt(0) == newString.charAt(newString.length - 1)){
		newString = newString.slice(1, newString.length - 1);
		if(newString.length != 0){
			return check_palindrome(newString);
		}
		else{
			return true;
		}
	}
	else{
		return false;
	}
}
