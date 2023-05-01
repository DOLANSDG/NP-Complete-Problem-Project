# NP-Complete-Problem-Project
This is my, Dawson Dolansky, solution to creating the exact and approximate solutions to Max Clique.

## Solutions
Both the exact and approximate solutions are stored in the *exact solutions* directory

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
The test cases differ in vertex size for the exact and approximate solutions. Both utilize the same test cases for each vertex size, but the exact solution due to runtime only include test cases that run under 20 minutes. 
That means that to test the 20 minutes case, you can run the following command.

<code> cat ./test_cases/gen_2998_edges_90_vertices.txt | python cs412_maxclique_exact.py </code> for the Bron-Kerbosch implementation.

and

<code> cat ./test_cases/gen_257_edges_27_vertices.txt | python cs412_maxclique_exact_non_bron_kerbosch.py </code> for a more general implementation that finds all subsets

## Presentations
My presentation slides for exact and approximation.

## Tools
Contains data tables of my testing of test cases and the graphing algorithm used.
