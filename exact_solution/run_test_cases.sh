#!/bin/sh
TEST_EXACT_FILES_PATH="./test_cases/exact_test_cases/*"
TEST_APPROXIMATION_FILES_PATH="./test_cases/approximation_test_cases/*"
echo "================================================="
echo

echo "This script created by Dawson Dolansky is for the purpose of running the exact and approximate solutions of all test cases"

echo
echo "================================================="

echo
echo "================================================="
echo "APPROXIMATION SOLUTIONS"
echo "================================================="
for filename in $TEST_APPROXIMATION_FILES_PATH
do
    echo "Finding the exact solution for $filename"
    ./run_approximation_test_cases.sh $filename
    echo
    echo "================================================="
done

echo
echo "================================================="
echo "EXACT SOLUTIONS"
echo "================================================="
for filename in $TEST_EXACT_FILES_PATH
do
     echo "Finding the exact solution for $filename"
    ./run_exact_test_cases.sh $filename
    echo
    echo "================================================="
done

echo "================================================="
echo



