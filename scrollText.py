#!/usr/bin/env python
#coding: utf8 
import time
import array
import fcntl
import sys
import math
import select
from ast import literal_eval

# 
# Open SPI device
spidev = file("/dev/spidev0.0", "wb")
#byte array to store rgb values
rgb=bytearray(3)
#setting spi frequency to 400kbps
fcntl.ioctl(spidev, 0x40046b04, array.array('L', [400000]))

#creating 10x10 matrix (last digit may be used later for alpha control)
matrix = [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
		  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
		  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
		  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
		  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
		  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
		  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
		  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
		  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
		  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]

cmatrix = [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]

			
#Define Functions for Allocation and Display
def allocate():
	#same as imgdisp.py, but with mirror so that 0/0 is at the upper left corner
	#Matrix is technically in reverse. X-Axis is horizontal, Y-Axis Vertical.
	#print "Allocating..."
	for x in range(0,10):
		for y in range (0,10):
			cmatrix[x][y][0] = matrix[x][y][0] 
			cmatrix[x][y][1] = matrix[x][y][1] 
			cmatrix[x][y][2] = matrix[x][y][2]
			
			#Column 1
			col = 1
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1] 
				cmatrix[x][y][2] = matrix[col][9][2]			
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]			
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]	
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]	
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]
				
				#Column 3
			col = 3
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1] 
				cmatrix[x][y][2] = matrix[col][9][2]			
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]			
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]	
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]	
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]
				
				#Column 5
			col = 5
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1] 
				cmatrix[x][y][2] = matrix[col][9][2]			
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]			
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]	
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]	
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]
			
			#Column 7
			col = 7
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1] 
				cmatrix[x][y][2] = matrix[col][9][2]			
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]			
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]	
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]	
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]
				
				#Column 9
			col = 9
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1] 
				cmatrix[x][y][2] = matrix[col][9][2]			
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]			
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]	
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]	
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]
				
	cmatrix.reverse()
				
def display():
	#allocating
	allocate()
	for x in range(0, 10):
		for y in range(0, 10):	
			rgb[0] = cmatrix[x][y][0]
			rgb[1] = cmatrix[x][y][1]
			rgb[2] = cmatrix[x][y][2]
			spidev.write(rgb)
								
	spidev.flush() 
			
def clear():
	for x in range(0,10):
		for y in range(0,10):
			matrix[x][y][0] = 0
			matrix[x][y][1] = 0
			matrix[x][y][2] = 0



#Define Characters
#Possible Characters: 
#	Uppercase letters
# 	Numbers

#reference point on matrix (upper left corner of bitmap)
def getChar(char, x, y):
	dic = {"A":[[x+1,y+7],[x+1,y+8],[x+2,y+5],[x+2,y+6],[x+3,y+3],[x+3,y+4],[x+3,y+5],[x+4,y+1],[x+4,y+2],[x+4,y+5],[x+5,y+1],[x+5,y+2],[x+5,y+5],[x+5,y+1],[x+6,y+3],[x+6,y+4],[x+6,y+5],[x+7,y+5],[x+7,y+6],[x+8,y+7],[x+8,y+8]],
		"B":[[x+1,y+1],[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+1,y+7],[x+1,y+8],[x+2,y+1],[x+2,y+4],[x+2,y+8],[x+3,y+1],[x+3,y+4],[x+3,y+8],[x+4,y+1],[x+4,y+4],[x+4,y+8],[x+5,y+1],[x+5,y+4],[x+5,y+8],[x+6,y+1],[x+6,y+4],[x+6,y+8],[x+7,y+2],[x+7,y+3],[x+7,y+5],[x+7,y+6],[x+7,y+7]],
		"C":[[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+2,y+2],[x+2,y+7],[x+3,y+1],[x+3,y+8],[x+4,y+1],[x+4,y+8],[x+5,y+1],[x+5,y+8],[x+6,y+1],[x+6,y+8],[x+7,y+2],[x+7,y+7]],
		"D":[[x+1,y+1],[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+1,y+7],[x+1,y+8],[x+2,y+1],[x+2,y+8],[x+3,y+1],[x+3,y+8],[x+4,y+1],[x+4,y+8],[x+5,y+1],[x+5,y+8],[x+6,y+1],[x+6,y+8],[x+7,y+2],[x+7,y+3],[x+7,y+4],[x+7,y+5],[x+7,y+6],[x+7,y+7]],
		"E":[[x+1,y+1],[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+1,y+7],[x+1,y+8],[x+2,y+1],[x+2,y+4],[x+2,y+8],[x+3,y+1],[x+3,y+4],[x+3,y+8],[x+4,y+1],[x+4,y+4],[x+4,y+8],[x+5,y+1],[x+5,y+4],[x+5,y+8],[x+6,y+1],[x+6,y+4],[x+6,y+8],[x+7,y+1],[x+7,y+4],[x+7,y+8],[x+8,y+1],[x+8,y+8]],
		"F":[[x+1,y+1],[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+1,y+7],[x+1,y+8],[x+2,y+1],[x+2,y+4],[x+3,y+1],[x+3,y+4],[x+4,y+1],[x+4,y+4],[x+5,y+1],[x+5,y+4],[x+6,y+1],[x+6,y+4],[x+7,y+1],[x+7,y+4],[x+8,y+1]],
		"G":[[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+2,y+2],[x+2,y+7],[x+3,y+1],[x+3,y+8],[x+4,y+1],[x+4,y+8],[x+5,y+1],[x+5,y+5],[x+5,y+8],[x+6,y+1],[x+6,y+5],[x+6,y+8],[x+7,y+2],[x+7,y+5],[x+7,y+6],[x+7,y+7]],
		"H":[[x+1,y+1],[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+1,y+7],[x+1,y+8],[x+2,y+4],[x+3,y+4],[x+4,y+4],[x+5,y+4],[x+6,y+4],[x+7,y+4],[x+8,y+1],[x+8,y+2],[x+8,y+3],[x+8,y+4],[x+8,y+5],[x+8,y+6],[x+8,y+7],[x+8,y+8]],
		"I":[[x+1,y+1],[x+1,y+8],[x+2,y+1],[x+2,y+8],[x+3,y+1],[x+3,y+8],[x+4,y+1],[x+4,y+2],[x+4,y+3],[x+4,y+4],[x+4,y+5],[x+4,y+6],[x+4,y+7],[x+4,y+8],[x+5,y+1],[x+5,y+8],[x+6,y+1],[x+6,y+8],[x+7,y+1],[x+7,y+8]],
		"J":[[x+2,y+6],[x+2,y+7],[x+3,y+8],[x+4,y+1],[x+4,y+8],[x+5,y+1],[x+5,y+8],[x+6,y+1],[x+6,y+8],[x+7,y+1],[x+7,y+2],[x+7,y+3],[x+7,y+4],[x+7,y+5],[x+7,y+6],[x+7,y+7]],
		"K":[[x+1,y+1],[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+1,y+7],[x+1,y+8],[x+2,y+5],[x+3,y+5],[x+4,y+4],[x+4,y+5],[x+5,y+3],[x+5,y+6],[x+6,y+2],[x+6,y+7],[x+7,y+1],[x+7,y+8]],
		"L":[[x+1,y+1],[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+1,y+7],[x+1,y+8],[x+2,y+8],[x+3,y+8],[x+4,y+8],[x+5,y+8],[x+6,y+8],[x+7,y+8]],
		"M":[[x+1,y+1],[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+1,y+7],[x+1,y+8],[x+2,y+2],[x+3,y+3],[x+4,y+4],[x+5,y+4],[x+6,y+3],[x+7,y+2],[x+8,y+1],[x+8,y+2],[x+8,y+3],[x+8,y+4],[x+8,y+5],[x+8,y+6],[x+8,y+7],[x+8,y+8]],
		"N":[[x+1,y+1],[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+1,y+7],[x+1,y+8],[x+2,y+2],[x+3,y+3],[x+4,y+4],[x+5,y+5],[x+6,y+6],[x+7,y+7],[x+8,y+1],[x+8,y+2],[x+8,y+3],[x+8,y+4],[x+8,y+5],[x+8,y+6],[x+8,y+7],[x+8,y+8]],
		"O":[[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+1,y+7],[x+2,y+1],[x+2,y+8],[x+3,y+1],[x+3,y+8],[x+4,y+1],[x+4,y+8],[x+5,y+1],[x+5,y+8],[x+6,y+1],[x+6,y+8],[x+7,y+1],[x+7,y+8],[x+8,y+2],[x+8,y+3],[x+8,y+4],[x+8,y+5],[x+8,y+6],[x+8,y+7]],
		"P":[[x+1,y+1],[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+1,y+7],[x+1,y+8],[x+2,y+1],[x+2,y+4],[x+3,y+1],[x+3,y+4],[x+4,y+1],[x+4,y+4],[x+5,y+1],[x+5,y+4],[x+6,y+1],[x+6,y+4],[x+7,y+2],[x+7,y+3]],
		"Q":[[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+2,y+1],[x+2,y+7],[x+3,y+1],[x+3,y+7],[x+4,y+1],[x+4,y+7],[x+5,y+1],[x+5,y+7],[x+6,y+1],[x+6,y+7],[x+7,y+1],[x+7,y+7],[x+7,y+8],[x+8,y+2],[x+8,y+3],[x+8,y+4],[x+8,y+5],[x+8,y+6],[x+8,y+8]],
		"R":[[x+1,y+1],[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+1,y+7],[x+1,y+8],[x+2,y+1],[x+2,y+4],[x+3,y+1],[x+3,y+4],[x+4,y+1],[x+4,y+4],[x+5,y+1],[x+5,y+4],[x+6,y+1],[x+6,y+4],[x+7,y+2],[x+7,y+3],[x+3,y+5],[x+4,y+6],[x+5,y+7],[x+6,y+8]],
		"S":[[x+2,y+2],[x+2,y+3],[x+2,y+7],[x+3,y+1],[x+3,y+4],[x+3,y+8],[x+4,y+1],[x+4,y+4],[x+4,y+8],[x+5,y+1],[x+5,y+4],[x+5,y+8],[x+6,y+1],[x+6,y+4],[x+6,y+8],[x+7,y+2],[x+7,y+5],[x+7,y+6],[x+7,y+7]],
		"T":[[x+1,y+1],[x+2,y+1],[x+3,y+1],[x+4,y+1],[x+4,y+2],[x+4,y+3],[x+4,y+4],[x+4,y+5],[x+4,y+6],[x+4,y+7],[x+4,y+8],[x+5,y+1],[x+6,y+1],[x+7,y+1]],
		"U":[[x+1,y+1],[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+1,y+7],[x+2,y+8],[x+3,y+8],[x+4,y+8],[x+5,y+8],[x+6,y+8],[x+7,y+8],[x+8,y+1],[x+8,y+2],[x+8,y+3],[x+8,y+4],[x+8,y+5],[x+8,y+6],[x+8,y+7]],
		"V":[[x+1,y+1],[x+1,y+2],[x+2,y+3],[x+2,y+4],[x+3,y+5],[x+3,y+6],[x+4,y+7],[x+4,y+8],[x+5,y+5],[x+5,y+6],[x+6,y+3],[x+6,y+4],[x+7,y+1],[x+7,y+2]],
		"W":[[x+1,y+1],[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+1,y+7],[x+1,y+8],[x+2,y+7],[x+3,y+6],[x+4,y+5],[x+5,y+5],[x+6,y+6],[x+7,y+7],[x+8,y+1],[x+8,y+2],[x+8,y+3],[x+8,y+4],[x+8,y+5],[x+8,y+6],[x+8,y+7],[x+8,y+8]],
		"X":[[x+1,y+1],[x+1,y+8],[x+2,y+2],[x+2,y+7],[x+3,y+3],[x+3,y+6],[x+4,y+4],[x+4,y+5],[x+5,y+4],[x+5,y+5],[x+6,y+3],[x+6,y+6],[x+7,y+2],[x+7,y+7],[x+8,y+1],[x+8,y+8]],
		"Y":[[x+1,y+1],[x+2,y+2],[x+3,y+3],[x+4,y+4],[x+4,y+5],[x+4,y+6],[x+4,y+7],[x+4,y+8],[x+5,y+3],[x+6,y+2],[x+7,y+1]],
		"Z":[[x+1,y+1],[x+2,y+1],[x+3,y+1],[x+4,y+1],[x+5,y+1],[x+6,y+1],[x+7,y+1],[x+8,y+1],[x+2,y+7],[x+3,y+6],[x+4,y+5],[x+5,y+4],[x+6,y+3],[x+7,y+2],[x+1,y+8],[x+2,y+8],[x+3,y+8],[x+4,y+8],[x+5,y+8],[x+6,y+8],[x+7,y+8],[x+8,y+8]],
		" ":[],
		"1":[[x+2,y+8],[x+3,y+2],[x+3,y+8],[x+4,y+1],[x+4,y+2],[x+4,y+3],[x+4,y+4],[x+4,y+5],[x+4,y+6],[x+4,y+7],[x+4,y+8],[x+5,y+8],[x+6,y+8]],
		"2":[[x+1,y+2],[x+1,y+8],[x+2,y+1],[x+2,y+7],[x+2,y+8],[x+3,y+1],[x+3,y+6],[x+3,y+8],[x+4,y+1],[x+4,y+5],[x+4,y+8],[x+5,y+1],[x+5,y+5],[x+5,y+8],[x+6,y+1],[x+6,y+4],[x+6,y+8],[x+7,y+2],[x+7,y+3],[x+7,y+8]],
		"3":[[x+1,y+2],[x+1,y+7],[x+2,y+1],[x+2,y+4],[x+2,y+8],[x+3,y+1],[x+3,y+4],[x+3,y+8],[x+4,y+1],[x+4,y+4],[x+4,y+8],[x+5,y+1],[x+5,y+4],[x+5,y+8],[x+6,y+1],[x+6,y+4],[x+6,y+8],[x+7,y+2],[x+7,y+3],[x+7,y+5],[x+7,y+6],[x+7,y+7]],
		"4":[[x+1,y+6],[x+2,y+5],[x+2,y+6],[x+3,y+4],[x+3,y+6],[x+4,y+3],[x+4,y+6],[x+5,y+2],[x+5,y+6],[x+6,y+1],[x+6,y+2],[x+6,y+3],[x+6,y+4],[x+6,y+5],[x+6,y+6],[x+6,y+7],[x+6,y+8],[x+7,y+6]],
		"5":[[x+1,y+1],[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+7],[x+2,y+1],[x+2,y+4],[x+2,y+8],[x+3,y+1],[x+3,y+4],[x+3,y+8],[x+4,y+1],[x+4,y+4],[x+4,y+8],[x+5,y+1],[x+5,y+4],[x+5,y+8],[x+6,y+1],[x+6,y+4],[x+6,y+8],[x+7,y+1],[x+7,y+5],[x+7,y+6],[x+7,y+7]],
		"6":[[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+1,y+7],[x+2,y+1],[x+2,y+4],[x+2,y+8],[x+3,y+1],[x+3,y+4],[x+3,y+8],[x+4,y+1],[x+4,y+4],[x+4,y+8],[x+5,y+1],[x+5,y+4],[x+5,y+8],[x+6,y+1],[x+6,y+4],[x+6,y+8],[x+7,y+5],[x+7,y+6],[x+7,y+7]],
		"7":[[x+1,y+1],[x+1,y+8],[x+2,y+1],[x+2,y+7],[x+3,y+1],[x+3,y+6],[x+4,y+1],[x+4,y+5],[x+5,y+1],[x+5,y+4],[x+6,y+1],[x+6,y+3],[x+7,y+1],[x+7,y+2]],
		"8":[[x+1,y+2],[x+1,y+3],[x+1,y+5],[x+1,y+6],[x+1,y+7],[x+2,y+1],[x+2,y+4],[x+2,y+8],[x+3,y+1],[x+3,y+4],[x+3,y+8],[x+4,y+1],[x+4,y+4],[x+4,y+8],[x+5,y+1],[x+5,y+4],[x+5,y+8],[x+6,y+1],[x+6,y+4],[x+6,y+8],[x+7,y+2],[x+7,y+3],[x+7,y+5],[x+7,y+6],[x+7,y+7]],
		"9":[[x+1,y+2],[x+1,y+3],[x+2,y+1],[x+2,y+4],[x+2,y+8],[x+3,y+1],[x+3,y+4],[x+3,y+8],[x+4,y+1],[x+4,y+4],[x+4,y+8],[x+5,y+1],[x+5,y+4],[x+5,y+8],[x+6,y+1],[x+6,y+4],[x+6,y+8],[x+7,y+2],[x+7,y+3],[x+7,y+5],[x+7,y+6],[x+7,y+7]],
		"0":[[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+1,y+7],[x+2,y+1],[x+2,y+7],[x+2,y+8],[x+3,y+1],[x+3,y+6],[x+3,y+8],[x+4,y+1],[x+4,y+5],[x+4,y+8],[x+5,y+1],[x+5,y+4],[x+5,y+8],[x+6,y+1],[x+6,y+3],[x+6,y+8],[x+7,y+2],[x+7,y+3],[x+7,y+4],[x+7,y+5],[x+7,y+6],[x+7,y+7]],
		":":[[x+4,y+3],[x+4,y+6]],
		";":[[x+4,y+3],[x+4,y+6],[x+3,y+7]],
		".":[[x+4,y+8]],
		",":[[x+4,y+8],[x+5,y+7]],
		"!":[[x+4,y+1],[x+4,y+2],[x+4,y+3],[x+4,y+4],[x+4,y+5],[x+4,y+6],[x+4,y+8]],
		"?":[[x+2,y+2],[x+3,y+1],[x+4,y+1],[x+4,y+5],[x+4,y+6],[x+4,y+8],[x+5,y+1],[x+5,y+5],[x+6,y+1],[x+6,y+5],[x+7,y+2],[x+7,y+3],[x+7,y+4]],
		'"':[[x+3,y+1],[x+3,y+2],[x+5,y+1],[x+5,y+2]],
		"#":[[x+1,y+3],[x+1,y+6],[x+2,y+3],[x+2,y+6],[x+3,y+1],[x+3,y+2],[x+3,y+3],[x+3,y+4],[x+3,y+5],[x+3,y+6],[x+3,y+7],[x+3,y+8],[x+4,y+3],[x+4,y+6],[x+5,y+3],[x+5,y+6],[x+6,y+1],[x+6,y+2],[x+6,y+3],[x+6,y+4],[x+6,y+5],[x+6,y+6],[x+6,y+7],[x+6,y+8],[x+7,y+3],[x+7,y+6],[x+8,y+3],[x+8,y+6]],
		"$":[[x+1,y+3],[x+1,y+7],[x+2,y+2],[x+2,y+4],[x+2,y+7],[x+3,y+2],[x+3,y+4],[x+3,y+7],[x+4,y+1],[x+4,y+2],[x+4,y+3],[x+4,y+4],[x+4,y+5],[x+4,y+6],[x+4,y+7],[x+4,y+8],[x+5,y+2],[x+5,y+4],[x+5,y+7],[x+6,y+2],[x+6,y+4],[x+6,y+7],[x+7,y+2],[x+7,y+5],[x+7,y+6]],
		"%":[[x+1,y+2],[x+1,y+3],[x+1,y+8],[x+2,y+1],[x+2,y+4],[x+2,y+7],[x+3,y+1],[x+3,y+4],[x+3,y+6],[x+4,y+2],[x+4,y+3],[x+4,y+5],[x+5,y+4],[x+5,y+6],[x+5,y+7],[x+6,y+3],[x+6,y+5],[x+6,y+8],[x+7,y+2],[x+7,y+5],[x+7,y+8],[x+8,y+1],[x+8,y+6],[x+8,y+7]],
		"&":[[x+1,y+2],[x+1,y+3],[x+1,y+4],[x+1,y+7],[x+2,y+1],[x+2,y+5],[x+2,y+6],[x+2,y+8],[x+3,y+1],[x+3,y+5],[x+3,y+8],[x+4,y+1],[x+4,y+4],[x+4,y+6],[x+4,y+8],[x+5,y+1],[x+5,y+3],[x+5,y+6],[x+5,y+8],[x+6,y+2],[x+6,y+7],[x+7,y+6],[x+7,y+8]],
		"'":[[x+4,y+1],[x+4,y+2]],
		"(":[[x+3,y+4],[x+3,y+5],[x+4,y+3],[x+4,y+6],[x+5,y+2],[x+5,y+7],[x+6,y+1],[x+6,y+8]],
		")":[[x+5,y+4],[x+5,y+5],[x+4,y+3],[x+4,y+6],[x+3,y+2],[x+3,y+7],[x+2,y+1],[x+2,y+8]],
		"*":[[x+2,y+1],[x+2,y+5],[x+3,y+2],[x+3,y+4],[x+4,y+1],[x+4,y+2],[x+4,y+3],[x+4,y+4],[x+4,y+5],[x+5,y+2],[x+5,y+4],[x+6,y+1],[x+6,y+5]],
		"+":[[x+2,y+5],[x+3,y+5],[x+4,y+3],[x+4,y+4],[x+4,y+5],[x+4,y+6],[x+4,y+7],[x+5,y+5],[x+6,y+5]],
		"-":[[x+2,y+5],[x+3,y+5],[x+4,y+5],[x+5,y+5],[x+6,y+5]],
		"/":[[x+1,y+8],[x+2,y+7],[x+3,y+6],[x+4,y+5],[x+5,y+4],[x+6,y+3],[x+7,y+2],[x+8,y+1]],
		"<":[[x+1,y+4],[x+2,y+3],[x+2,y+5],[x+3,y+3],[x+3,y+5],[x+4,y+2],[x+4,y+6],[x+5,y+2],[x+5,y+6]],
		">":[[x+5,y+4],[x+4,y+3],[x+4,y+5],[x+3,y+3],[x+3,y+5],[x+2,y+2],[x+2,y+6],[x+1,y+2],[x+1,y+6]],
		"=":[[x+2,y+3],[x+2,y+6],[x+3,y+3],[x+3,y+6],[x+4,y+3],[x+4,y+6],[x+5,y+3],[x+5,y+6],[x+6,y+3],[x+6,y+6]],
		"@":[[x+1,y+4],[x+1,y+5],[x+1,y+6],[x+2,y+3],[x+2,y+7],[x+3,y+2],[x+3,y+8],[x+4,y+1],[x+4,y+8],[x+5,y+1],[x+5,y+4],[x+5,y+5],[x+5,y+6],[x+5,y+8],[x+6,y+1],[x+6,y+4],[x+6,y+6],[x+6,y+8],[x+7,y+1],[x+7,y+4],[x+7,y+6],[x+7,y+8],[x+8,y+1],[x+8,y+2],[x+8,y+3],[x+8,y+4],[x+8,y+5],[x+8,y+6]],
		"^":[[x+2,y+3],[x+3,y+2],[x+4,y+1],[x+5,y+2],[x+6,y+3]],
		"_":[[x+1,y+8],[x+2,y+8],[x+3,y+8],[x+4,y+8],[x+5,y+8],[x+6,y+8],[x+7,y+8],[x+8,y+8]],
		"[":[[x+3,y+1],[x+3,y+2],[x+3,y+3],[x+3,y+4],[x+3,y+5],[x+3,y+6],[x+3,y+7],[x+3,y+8],[x+4,y+1],[x+4,y+8],[x+5,y+1],[x+5,y+8]],
		"]":[[x+5,y+1],[x+5,y+2],[x+5,y+3],[x+5,y+4],[x+5,y+5],[x+5,y+6],[x+5,y+7],[x+5,y+8],[x+4,y+1],[x+4,y+8],[x+3,y+1],[x+3,y+8]]}
		


	#print char
	return dic[char]


def getChars(text, x, y):
	#x = 0
	#y = 0
	charsPos = []
	chars = []
	length = len(text)
	#print "len: " + str(length)
	for i in range(0, length):
		try:
			if (-10 <= x <= 9):
				charsPos.extend(getChar(text[i],x,y))
				chars.append(text[i])
		except:
			pass
		x = x + 10
		#print ch4arsPos
		#print chars
	return charsPos



global speed
global color


def setSpeed(newSpeed):
	global speed
	if 1 >= newSpeed >= 0:
		speed = newSpeed
	print speed

def getSpeed():
	if (standardSpeed == speed) == False:
		#print "returned new Speed"
		return speed
	else:
		#print "returned standardSpeed"
		return standardSpeed

def setColor(newColor):
	global color
	color = newColor
	print color

def getColor(index):
	if(standardColor == color) == False:
		return int(color[index])
	else:
		return int(standardColor[index])

def checkInput():
#falls stdin vorhanden wird es auf input gespeichert
	if select.select([sys.stdin], [], [], 0)[0]:
		Input = sys.stdin.readline().strip().upper()
		
		if Input[0:7] == "*SPEED*":
			setSpeed(float(Input[7:len(Input)]))
		elif Input[0:7] == "*COLOR*":
			rgb = literal_eval(Input[7:len(Input)])
			setColor(rgb)
		else:			
			print Input
			play(Input.upper())

def setMatrix(parts):
	
	for i in range(0, len(parts)):
		try:
			a = parts[i][0]
			b = parts[i][1]
			
			if (a or b) < 0:
				#print "negative"
				pass
			else:
				matrix[a][b][0] = getColor(0)
				matrix[a][b][1] = getColor(1)
				matrix[a][b][2] = getColor(2)
				#print("part %i done" % i)
		except:
			#print "not on matrix!"
			pass



def main(Input,x,y):
	
	text = Input
	length = len(text)

	for i in range(0, length*10+10):
		checkInput()
		pixels = getChars(text,x,0)
		setMatrix(pixels)
		display()
		x = x -1
		#print speed
		time.sleep(getSpeed())
		clear()
	



standardSpeed = 0.025
speed = standardSpeed
standardColor = [255,0,0]
color = standardColor
passes = 0
#Input = raw_input("Text to display: ").upper()

"""
Commandline Argument input:
argv[1] = Text
argv[2] = speed
argv[3] = color
argv[4] = # Passes (0 = infinite)

"""
if len(sys.argv) < 2:
	Input = "HELLO"
else:
	try:
		Input = sys.argv[1].upper()
		setSpeed(float(sys.argv[2]))
		setColor(literal_eval(sys.argv[3]))
		passes = int(sys.argv[4])
	except:
		print "Failed to use arguments"

def play(Input):
	if passes == 0:
		while True:
			clear()
			checkInput()
			main(Input,10,0)
	else:
		for i in range(0, passes):
			clear()
			checkInput()
			main(Input,10,0)

print("Scrolling Text Initiated")
play(str(Input))
			
#abcdefghijklmnopqrstuvwxyz 1234567890.,:;-_+"@*#%&/()=?'^!$<>[]
