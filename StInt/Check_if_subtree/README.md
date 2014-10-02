Check if a one given tree is a subtree of the other given tree. 

APPROACH : Asuume there are two trees : Tree S and Tree T. 
Do a pre order traversal and inorder traversal of Tree S.
Do an inorder and pre order traversal of Tree T.
If S's inorder is a substring of T's inorder and S's pre-order is a substring of T's pre-order then its a subtree. 
