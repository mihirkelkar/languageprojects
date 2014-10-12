Find all the nodes which are at a distance of k from the leaf nodes. 

Appraoche One: 
1) Traverse the tree storing all elements level wise. 

2) Pass the ancestors in a list. 

3) When you hit a leaf node. Print the ancestor at index -k in the list. 

Approach Two:
1) Start traversing all nodes, next go ahead and calculate the depth to leaves from that node. Now, if the differnece between level and leaf level is k. Print it. 

I kinda like approacj two. Let me go ahead and code this. 


