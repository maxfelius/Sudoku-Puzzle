#! python3
'''
@author: Max Felius
@mail: maxfelius@hotmail.com

Sudoku solver
'''

#imports
import numpy as np
from matplotlib import pyplot as plt
import Sudoku1 as Sudoku

#The starting grid
grid = Sudoku.grid

class SudokuSolver:
    def __init__(self,puzzle):
        self.puzzle = puzzle

        self.solve()

    #Check if a number is possible in the grid
    def possible(self,y,x,n):
        for i in range(0,9):
            if self.puzzle[y][i] == n:
                return False
        for i in range(0,9):
            if self.puzzle[i][x] == n:
                return False

        x0 = (x//3)*3
        y0 = (y//3)*3
        
        for i in range(0,3):
            for j in range(0,3):
                if self.puzzle[y0+i][x0+j] == n:
                    return False
        return True

    #The solve function
    def solve(self):
        for y in range(9):
            for x in range(9):
                if self.puzzle[y][x] == 0:
                    for n in range(1,10):
                        if self.possible(y,x,n):
                            self.puzzle[y][x] = n
                            
                            self.solve()

                            self.puzzle[y][x] = 0

                    return

        # Plot the results in a graph
        self.initiateFigure()

    def initiateFigure(self):    
        plt.figure(figsize=(5,5))
        
        text_style_number = dict(horizontalalignment='center', verticalalignment='center',
                                fontsize=14, fontdict={'family': 'monospace'}, weight='bold')
        
        #filling in the numbers
        for y in range(9):
            for x in range(9):
                if self.puzzle[y][x] == 0:
                    #skip
                    continue
                else:
                    plt.text(x+0.5,8.5-y,str(self.puzzle[y][x]),**text_style_number)
        
        #creating the gridlines
        for n in range(9):
            if n==3 or n==6:
                plt.axhline(n, linewidth=3, color= 'r')
                plt.axvline(n, linewidth=3, color='r')
            else:
                plt.axhline(n, linewidth=1, color= 'k')
                plt.axvline(n, linewidth=1, color='k')
            
        plt.axis([0,9,0,9])
        plt.show()

#Starting to solve the matrix
if __name__ == '__main__':
    SudokuSolver(grid)


