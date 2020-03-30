#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:36:22 2020

@author: Max Felius
@mail: maxfelius@hotmail.com
"""

#imports
import numpy as np
from matplotlib import pyplot as plt
import copy

#INPUT SUDOKO
puzzle = np.array([
    [6,0,0,0,9,0,0,5,0],
    [0,8,9,0,0,0,4,6,0],
    [0,0,4,6,3,0,0,0,7],
    [0,7,5,0,6,0,1,0,2],
    [0,4,1,0,0,0,6,8,0],
    [9,0,3,0,2,0,7,4,0],
    [4,0,0,0,5,7,2,0,0],
    [0,1,8,0,0,0,5,7,0],
    [0,2,0,0,8,0,0,0,4]])

class SudokuSolver:
    def __init__(self,puzzle,displaySolution=True):
        self.puzzle = puzzle
        self.puzzleSolved = copy.deepcopy(puzzle)
        
        #Start solving the sudoku
        self.SolveSudoku()
        
        if displaySolution == True:
            self.initiateFigure()
        
    def SolveSudoku(self):
        #set start position
        row = 0
        column = 0
        
        while True:
            if row == 9 or column == 9:
                print('Finished bruteforcing the Sudoku...')
                break 
            
            if self.checkGiven(row,column):
                row, column = self.nextStep(row,column)        
                continue
            
            else:
                number = self.Backtrack(row,column,1)        
                self.puzzleSolved[row,column] = number
                
                row, column = self.nextStep(row,column)
    
    def getbox(self,row,column):
      		def position(place):
      			if place > 2:
      				if place > 5:
      					placeBox = [6,9]
      				else:
      					placeBox = [3,6]
      			else:
      				placeBox = [0,3]
      			return placeBox
      
      		rowIndex = position(row)
      		columnIndex = position(column)
      
      		return self.puzzleSolved[rowIndex[0]:rowIndex[1],columnIndex[0]:columnIndex[1]]
          
    def checkValid(self,row,column,i):   
        #rowCheck
        if i in self.puzzleSolved[:,column]:
            return False
    						
            #columnCheck
        elif i in self.puzzleSolved[row,:]:
            return False
    						
        #boxCheck
        elif i in self.getbox(row,column):
            return False
        
        else:
            return True
    
    def nextStep(self,row,column):
        if column == 8:
            row = row + 1
            column = 0
            
        else:
            column = column + 1
        
        if self.checkGiven(row,column):
            row, column = self.nextStep(row,column)
        
        return row,column
    
    def checkGiven(self,row,column):
        if row == 9 or column == 9:
            return False
        if self.puzzle[row,column] != 0:
            return True
        else:
            return False
    
    def previousStep(self,row,column,step=1):    
        for i in range(step):
            if column == 0:
                row = row - 1
                column = 8   
                assert row > 0,'Row can\'t be negative.'             
            else:
                column = column - 1
            
            if self.checkGiven(row,column):
                row, column = self.previousStep(row,column)
        
        return row, column
        
    def newNumber(self,number):
        if number == 9:
            return 1
        else:
            return number + 1
      
    def checkCurrentTile(self,row,column,number):
        for _ in range(9):
            if self.checkValid(row,column,number):
                return number
            else:
                number = self.newNumber(number)
        return False
    
    def backtrackNewNumber(self,prow,pcolumn,start_number):
        #this function return the next valid number
        #edit previous number                                                       
        pnumber = self.puzzleSolved[prow,pcolumn]
        
        self.puzzleSolved[prow,pcolumn] = 0
        
        while True:    
            pnumber = self.newNumber(pnumber)
            
            if start_number == pnumber:
                self.puzzleSolved[prow,pcolumn] = pnumber
                return False
                
            if self.checkValid(prow,pcolumn,pnumber):
                self.puzzleSolved[prow,pcolumn] = pnumber
                return True
    
    def Backtrack(self,row,column,number):
        #set falg
        flag = True
        
        #Make copy of current sudoka for selecting starting numbers
        puzzleSolvedCopy = copy.deepcopy(self.puzzleSolved)
        
        while True:
            out = self.checkCurrentTile(row,column,number)
        
            if type(out) == int:
                #return the number for the new tile
                return out
            else:
                #set first level depth (previous tile)
                depth = 1
                while True:
                    prow, pcolumn = self.previousStep(row,column,depth)
                    flag = self.backtrackNewNumber(prow,pcolumn,puzzleSolvedCopy[prow,pcolumn])
                    if flag == False:
                        #go one level deeper (one extra tile back)
                        depth +=1
                    else:
                        break
        
    def initiateFigure(self):
        plt.figure(figsize=(5,5))
        
        text_style_number = dict(horizontalalignment='center', verticalalignment='center',
                                fontsize=14, fontdict={'family': 'monospace'}, weight='bold')
        
        #filling in the numbers
        for y in range(9):
            for x in range(9):
                if self.puzzleSolved[y,x] == 0:
                    #skip
                    continue
                else:
                    plt.text(x+0.5,8.5-y,str(self.puzzleSolved[y,x]),**text_style_number)
            
        
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
        

if __name__ == '__main__':
    SudokuSolver(puzzle)
