Given a binary tree, check if its a BST. 


Solution: Start doing an inorder traversal of the tree. Keep track of the values of the previous nodes. If at any point in the whole process, the value of the previous node is greater than the value of the current node, then its a violation. 

