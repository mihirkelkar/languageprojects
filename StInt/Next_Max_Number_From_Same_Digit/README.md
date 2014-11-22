Construct the next max digit from the same digits. 

Solution could be as follows:
  Start from the last element. Start iterating through towards the first. 
  Find the first time when the left element is smaller than the right element
  eg. 

  123 4 7654321
  Now, look at everything to the right of the next element. 
  Find the smallestelement which is just larger than this element. 
  Which is 5
  123 5 4 763421 
