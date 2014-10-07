ALGORITHM GOLD : BOUNDARY TRAVERSAL OF A TREE
=============================================
Given a binary tree, print the boundary nodes of the binary tree Anti-Clockwise starting from the root. 

We can break this problem up into the following parts: 
1) print the left boundary in the top-down manner
2. Print all leaf nodes from left to right, which can again be divided into 
two parts -->
        ------> Print all leaf nodes of left sub-tree from left to right
        ------> Print all leaf nodes of right sub-tree from left to right
3) Print the boundary in a bottom up fashion. 

Given a binary tree, print boundary nodes of the binary tree Anti-Clockwise starting from the root. For example, boundary traversal of the following tree is “20 8 4 10 14 25 22″
http://www.geeksforgeeks.org/boundary-traversal-of-binary-tree/

