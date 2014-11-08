You're given binary tree as a sequence of (parent,child) tuples. In this representation, for example the given tree is represented as

(A,B) (A,C) (B,G) (C,H) (E,F) (B,D) (C,E)
The same tree could be written as an s-expression

(A(B(D)(G))(C(E(F))(H)))
We'd like you to translate the first represenation into the second, and report errors if any.

The list of Errors codes are as follows:

Error Code      Type of error
E1                 More than 2 children
E2                 Duplicate Edges
E3                 Cycle present
E4                 Multiple roots
E5                 Any other error   

NOTE:
1. there is no specific sequence in which the input (parent,child) pairs are represented.
2. The input tuples are separated by a single space.
3. The output tuples format has no spaces in it.
4. Assume there are maximum 26 nodes, each having a single character (from A-Z) as their data.
5. Error cases are to be handled by preference. For example, in case an input satisfies error cases 1 and 2, the output must be E1

Input Format:

Input must be read from standard input.
Input will consist of 1 line of parent-child pairs, each enclosed in a bracket and separated by a single space (as described above).

Output:

The function must write to standard output.
Output the given tree in the 2nd representation as described above. The general output structure is (Node(Left-child(...)(...))(Right-child(...)(...)))
There are no spaces in the output.


