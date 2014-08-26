var numbers_to_words_map = {
"1" :"one",
"2" : "t:wo",
"3" :"three",
"4": "four",
"5": "five" ,
"6":"six" ,
"7" :"seven" ,
"8" :"eight" ,
"9" :"nine" ,
"10": "ten" ,
"11": "eleven" ,
"12": "twelve" ,
"13": "thirteen" ,
"14": "fourteen" ,
"15": "fifteen" ,
"16": "sixteen" ,
"17": "seventeen" ,
"18": "eighteen" ,
"19": "nineteen" ,
"20": "twenty" ,
"30": "thirty" ,
"40": "fourty" ,
"50": "fifty" ,
"60": "sixty" ,
"70": "seventy" ,
"80": "eighty" ,
"90" :"ninty" 
}

function numbers_to_words(number){
  var words = "";	
  if((number % 100).toString() in numbers_to_words_map){
  	words += numbers_to_words_map[(number % 100).toString()];
  }
  else if((number % 10).toString() in numbers_to_words_map){
  	words += numbers_to_words_map[(number % 10).toString()];
  	words += numbers_to_words_map[((number % 100) - (number % 10)).toString()];
  }

  if((((number % 1000) - (number % 100)) / 100).toString() in numbers_to_words_map){
  	words += numbers_to_words_map[(((number % 1000) - (number % 100)) / 100).toString()];
  	words += 'hundred';
  }
  if ((number % 1000) == 0){
    words = words + numbers_to_words_map[(number / 1000).toString()] + 'thousand';
  }
  else if((number % 1000) != 0){
  	number = number.toString()[0];
  	words += numbers_to_words_map[number];
  	words += 'thousand';
  }
  //debug(words);
  return words.length;
}

//debug(numbers_to_words(6649));


var total_word_count_sum = 0;
for(i = 0; i <= 1000; i++){
	total_word_count_sum += numbers_to_words(i);
}

debug("Total sum of word counts of all numbers expressed as words is " + total_word_count_sum);


