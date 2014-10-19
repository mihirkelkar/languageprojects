The idea here is instead of doing an entire inorder traversal, what you do is keep a track of the nodes every node has in its left subtree. 
If there are n nodes in your left subtree and k is n + 1, then the root is the node you are looking for. 

if k < n : then recurse to the lower level . 

if k > n + 1 then go ahead and recurse on the right subtree. 
