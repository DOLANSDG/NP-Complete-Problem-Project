#!/bin/sh
TEST_FILES_PATH="./test_cases/"
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
for N_VERTICES in 10 20 21 22 23 24 25 26 27 30 40 50 60 70 80 90 100 110 120 130 140 150 160 170 180 190 200 210 220 230 240 250
do
    python generate_test_cases.py $N_VERTICES
done
echo
echo "================================================="
