 cyclic sorted list could look as follows: 

1  -->  3 --> 4 --> 5
 |		    |
 <-------------------

Basically I would have a loop which traverses the cyclic sorted list and find the point where I will be isnerting my given node


Lets assume that the value that I am about to insert into the loop is called X. prev --> val <= X <= current --> val. 

Then insert between current and prev. 

x is the max or the minimum of the list. 
--> Then just go ahead and add it to the end of the list. That will work. 
