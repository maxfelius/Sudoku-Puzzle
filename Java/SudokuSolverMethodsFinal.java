/*
@author: Max Felius
@email: maxfelius@hotmail.com

Sudoku Solver written in Java
 */

//import
import javax.swing.*;

class SudokuSolverMethodsFinal {
    //initiate variable
    public int[][] puzzle;

    //constructor
    public SudokuSolverMethodsFinal(int[][] input){
        puzzle = input;
    }
    
    //Method to check if the proposed number is possible
    boolean possible(int y, int x, int n){
        for (int i = 0; i < 9; i++){
            if (puzzle[y][i] == n){
                return false;
            }
        }
        for (int i = 0; i < 9; i++){
            if (puzzle[i][x] == n){
                return false;
            }        
        }

        int x0 = (x/3)*3;
        int y0 = (y/3)*3;

        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                if (puzzle[y0+i][x0+j] == n){
                    return false;
                }
            }
        }
        return true; 
    }

    //Method for plotting the resulting sudoku puzzle   
    void openFrame(int[][] mat) {
        System.out.println("Sudoku Puzzle\n");
        // Loop through all rows 
        for (int i = 0; i < mat.length; i++){
            if (i==3 || i == 6){
                System.out.print("---------------------\n");
            }
            // Loop through all elements of current row 
            for (int j = 0; j < mat[i].length; j++){
                if (j==3 || j == 6){
                    System.out.print("| ");
                } 
                System.out.print(mat[i][j] + " ");
            }
            System.out.print("\n");
        }
    }

    public void solve() {
	for (int y = 0; y < 9; y++) {
            for (int x = 0; x < 9; x++) {
                if (puzzle[y][x] == 0) {
                    for (int n = 1; n < 10; n++) {
                        if (possible(y, x, n)) {
                            puzzle[y][x] = n;

                            solve();

                            puzzle[y][x] = 0;
                        }
                    }
                    return;
                }
            }
        }
    openFrame(puzzle);    
    }

    public static void main(final String[] args) {
        //Global Variables
        Puzzle puzzleIn = new Puzzle();

        SudokuSolverMethodsFinal sudoku = new SudokuSolverMethodsFinal(puzzleIn.puzzle);

        sudoku.solve();
    }
}
