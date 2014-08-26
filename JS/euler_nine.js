for(var i = 1; i < 1000; i++){
  for(var j = 1; j < 1000; j++){
    for(var k = 1; k < 1000; k++){
        if(i + j + k == 1000){
          if( i * i + j * j == k * k){
            debug(i * j  * k); 
            debug(i);
            debug(j);
            debug(k);
            debug("===============")
            break;
          }
        }
      }
    }
  }
