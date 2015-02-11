Print a string in sinusoidal fashion. 

Example : 
  I
M   H   R
      I. 


Solution Idea : A good way to this would be to basically three buffers. Iterate through the string. If its a perfect mod 2. It goes to the central buffer. 
Else, it either goes to the up or down buffer. Every time I add something to one buffer, I add spaces to the other two buffers.  
