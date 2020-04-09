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
            //System.out.println(this.puzzle[y][i]);
            if (puzzle[y][i] == n){
                
                //System.out.println("Number in row");
                return false;
            }
        }
        for (int i = 0; i < 9; i++){
            if (puzzle[i][x] == n){
                //System.out.println("Number in column");
                return false;
            }        
        }
        int x0 = (x/3)*3;
        int y0 = (y/3)*3;
        //System.out.println("x0 "+x0+", y0 "+y0);
        for (int i = 0; i < 3; i++){
            for (int j = 0; j < 3; j++){
                if (puzzle[y0+i][x0+j] == n){
                    //System.out.println("Number in box");
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

    public static void print2D(int mat[][])
    { 
        // Loop through all rows 
        for (int i = 0; i < mat.length; i++) 
  
            // Loop through all elements of current row 
            for (int j = 0; j < mat[i].length; j++) 
                System.out.print(mat[i][j] + " "); 
    }

    public void solve() {
    //System.out.println("Started with the solver method");
	    for (int y = 0; y < 9; y++) {
            for (int x = 0; x < 9; x++) {
                //System.out.println("Location"+y+","+x);
                if (puzzle[y][x] == 0) {
                    for (int n = 1; n < 10; n++) {
                        //System.out.println("Test possible with number: "+n+". Test Possible: "+possible(y, x, n));
                        if (possible(y, x, n)) {
                            //System.out.println("set new number");
                            puzzle[y][x] = n;

                            //System.out.println("Start recursion");
                            solve();

                            //System.out.println("Set tile to zero");
                            puzzle[y][x] = 0;
                        }
                    }
                    //System.out.println("Return");
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
