var sum = 0;
//Return the sum of all even numbered terms of the fibonacci 
//sequence below four million
var sec = 1;
var fir = 0;
function fibo_iterative(){
	while(fir < 4000000){
		var temp = sec;
		sec = fir + sec;
		//debug(sec);
		fir = temp;
		if(sec % 2 == 0)
			{
				sum += sec;
			}
	}
	debug(sum);
}

fibo_iterative();
debug(sum);