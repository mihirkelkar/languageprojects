Let s be an array of strings. Write a function ehich finds the distance of any closest pair of equal entries. For example = 
<All, work, No, play, makes, for, no, work, no, fun, and, no, results>
here the minimum distance between no and no is 1. 

The way you do this is you itearte through the whole list of strings and maintain a hash with the string as a key and its most recent location as a value. Everytime you encounter a repeat, you calculate the differnece. If that is smaller than any previous minimum distance, you update it. You also update the record for that string in teh hash map. 
