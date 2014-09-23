We deal with the ase of single rotation only in two cases. 

1) An element is added to the left most subtree of the left subtree of the root. 
		          
                        Root
                       /   \
                      K1    C
                     /  \            
                    A    B
                  /
            Inserted 
              Node
    

then we can do a L-L Rotation to make the tree like this. 
  
                           K1     
                          /  \
                         A    Root
                        /    /  \
                 Inserted   B    C
                   Node. 


2) The other case that calls for a single rotation is when you add an element to the right most subtree of the right subtree of the root which calls for a right rotation. 

                      Root
                     /    \
                    K1     A
                          / \
                         B   C
                              \
                            Inserted
                              Node

        then we do a R-R rotation to make the tree balanced as it was previously

                      A
                    /   \
                  Root   C
                 /   \    \
                K1    B   Inserted 
                            Node

        
