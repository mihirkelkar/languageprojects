There are two inked lists which intersect at some point forming a "Y" like shape and have a common end. 

Find the first node which is common to both lists. 

Appraches I thought: Traverse one list and mark nodes as visited. Traverse other list till you hit a visited node. 

Approach 2: Hash the nodes, if you visit a node that has been hashed, then you are in luck . 

Appraoch 3: Traverse List one to calculate number of nodes : c1
            Traverse List two to calculate number of nodes : c2
            Find the difference between the number of nodes in both lists 
            diff = abs(c1 - c2).
            Trvaerse the list diff times. 
            Now, start traversing both lists at the same time checking if the node is same by direct comparison. 


