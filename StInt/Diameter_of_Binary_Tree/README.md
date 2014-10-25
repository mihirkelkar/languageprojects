The diameter of a tree is the number of nodes on the longest path between the two leaves in the tree. 

Maintain a variable that keeps track of the maximum length of path found so far.

The rest should be pretty straight forward. You calculate the max height of the
left subtree, you calculate the max height of the right subtree. 
You see of the path is longest. Store the path if its the longest. 
Pass up 1 + height of the tree. 

 
