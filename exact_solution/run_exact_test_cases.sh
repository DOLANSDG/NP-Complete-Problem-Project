#!/bin/sh
# Exact test cases script for only doing up to the case where it will be 20 minutes
FILE_NAME=$1
# Exact
echo "Exact:"
exact_output="$(cat $FILE_NAME | python cs412_maxclique_exact.py)"
echo "\tFound the Max Clique of $exact_output"
