# Running Python Code on a sample/test case
### Generating Test Cases
Although test cases are already generated to align with the data I got for the presentation, you can create new test cases as follows. 
1. Remove the test cases contained in the folders.
2. run the bash script *gen_test_cases.sh* while in the *exact solution* directory
   3. <code> ./gen_test_cases.sh </code>

### Testing the solutions
#### Running tests
To test the test cases with my approximation and exact solution implementations, you can run the following script as follows when in the *exact solutions* directory

<code> ./run_test_cases.sh </code>

#### Testing the 20 minutes exact solution case
The test cases differ in vertex size for the exact and approximate solutions. 
Both utilize the same test cases for each vertex size, but the exact solution due to runtime only include test cases that run under 20 minutes. 
That means that to test the 20 minutes case for either exact solution, you can run the following command.

<code> cat ./test_cases/gen_2998_edges_90_vertices.txt | python cs412_maxclique_exact.py </code> for the Bron-Kerbosch implementation.

and

<code> cat ./test_cases/gen_257_edges_27_vertices.txt | python cs412_maxclique_exact_non_bron_kerbosch.py </code> for a more general implementation that finds all subsets


# Test Cases Format and Details
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

Any test case beginning with "gen" is a generated test case from the generation scirpt