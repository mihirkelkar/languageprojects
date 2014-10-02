The challange here is given a binary tree. Construct a binary search tree such that is still has the structure of the binary tree. 

Eg. Given Binary Tree : 
        10
       /  \
      2    7
     /\   
    8  4


        8
       / \
      4   10
     /\
    2  7



Eg 2. 
        10
       /  \
      30   15
     /      \
    20       5


gets converted to 
     
        15
       /  \
      10   20
     /       \
    5         30

The approach here is do an inorder traversal of the given binary tree and copy the results into a list. Sort the list and do an inorder traversal of the tree 
again, copy the array elements into it. 

You now have a binary search tree with the same structure.    
