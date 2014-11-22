Find the distance between 2 nodes of a binary tree, no parent pointers are available. Distance between two nodes is the minimum number of edges to be traversed to reach one node from the other.


The idea is basically follow the lowest common ancestor: 

Find Lowest commpn Ancestor. 
The idea is to find the distance from the root to node1, find the distance from root to node2 and then subtract 2 * distance between root to lca 
