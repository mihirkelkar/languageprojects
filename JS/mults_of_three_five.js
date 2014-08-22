//Project Euler question No. 1
var counter = 0;
var sum = 0
while(counter < 1000){
  if(counter % 3 == 0){
    sum += counter;
  }
  if(counter % 5 == 0){
  	sum += counter;
  }
  counter++;
}
//Hack around because jsc in mac doesn't take console.log for some
//reason
debug(sum);