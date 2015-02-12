Find the least common ancestor of two nodes in the binary tree (Not a binary search tree)
The idea is simple:
  You recur on the left subtree and the right subtree at every node. 
  You get answers as to whether any one of the nodes in present in either sides. 

  If you come across a situation where one node is on either sides. Thats your
  answer
