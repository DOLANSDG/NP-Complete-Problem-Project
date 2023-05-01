#!/bin/sh
# Exact test cases script for only doing up to the case where it will be 20 minutes
FILE_NAME=$1
# Approximate
echo "Approximation:"
approximation_output="$(cat $FILE_NAME | python cs412_maxclique_approx.py)"
echo "\tFound the Max Clique of $approximation_output"
