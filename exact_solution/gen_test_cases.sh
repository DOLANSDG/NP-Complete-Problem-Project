#!/bin/sh
TEST_FILES_PATH="./test_cases/*"
echo "================================================="
echo

echo "This script created by Dawson Dolansky is for the purpose of generating the test cases"

echo
echo "================================================="

# generate test cases
echo
echo "================================================="
echo
echo "Generating test cases of random edges with vertex counts of {5, 25, 125}"
echo
python generate_test_cases.py 50 ./test_cases/
for N_VERTICES in 5 25
do
# three trials
python generate_test_cases.py $N_VERTICES ./test_cases/
python generate_test_cases.py $N_VERTICES ./test_cases/
python generate_test_cases.py $N_VERTICES ./test_cases/
done
echo
echo "================================================="
