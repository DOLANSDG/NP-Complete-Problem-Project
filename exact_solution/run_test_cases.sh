#!/bin/sh
TEST_FILES_PATH="./test_cases/*"
echo "================================================="
echo

echo "This script created by Dawson Dolansky is for the purpose of running the exact and approximate solutions of all test cases \n\t$1"

echo
echo "================================================="

# Remove test cases generated
cd "./test_cases/"
rm *gen*
cd ..

# filename
for filename in $TEST_FILES_PATH
do
    echo
    echo "Running Solutions on $filename"
    echo

    # Exact
    echo "Exact:"
    exact_output="$(cat $filename | python Optimal_Max_Clique.py)"
    echo "\tFound the Max Clique of {$exact_output}"

    # Approximate
    echo "Approximation:"
    approximation_output="$(cat $filename | python Approximation_Max_Clique.py)"
    echo "\tFound the Max Clique of {$approximation_output}"

    echo
    echo "================================================="
done

echo "================================================="
echo



