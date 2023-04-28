# Running Python Code on a sample/test case
## Script
Utilizing the bash script run_test_cases.sh, all of the supplied and created test cases are run iteratively, with output of the max clique found for
both the exact and approximation solutions.

## Manual Testing
This can be done by the following cmdline input

<code> python Optimal_Max_Clique.py graph_input_filename.txt </code>

or similarily

<code> python Optimal_Max_Clique.py graph_input_filename.txt </code>

# Test Cases
## Stores test cases for Max Clique Algorithms
### Format
For Max Clique the input is an undirected graph. The first line will list the number of edges m. The remaining m lines will be a flat edge list with the edges specified only once.
The vertices are inferred from the edge list. 

## quick details of each
0. no nodes or no edges
1. one node;  1 node; loop edge
2. two nodes that are connected; 2 nodes; 1 edge
3. 3 node complete graph
4. 2 "3 node complete graphs" connected by a middle vertex; Testing two equal maximal cliques
5. Textbook Independent Set to Max Clique Graph; 8 nodes; 16 edges
6. Wikipedia Example; 6 nodes; 7 edges

There is an additional test case given by Dr. Molloy for a larger graph.