# Script for running the program from the terminal
# Run "chmod 755 ./runner.sh" if you get a permission error

# Java Script to be run
# The ".java" part should be omitted
PROGRAM="SudokuSolverMethodsFinal"

javac "${PROGRAM}.java"

echo "Compiled the ${PROGRAM}"

java $PROGRAM
