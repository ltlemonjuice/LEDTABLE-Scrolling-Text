#!/usr/bin/env python
import time
import array
import fcntl
import sys
import math
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
		print chars
	return charsPos


def setMatrix(parts):
	
	for i in range(0, len(parts)):
		try:
			a = parts[i][0]
			b = parts[i][1]
			
			if (a or b) < 0:
				#print "negative"
				pass
			else:
				matrix[a][b][0] = 255
				matrix[a][b][1] = 0
				matrix[a][b][2] = 0
				#print("part %i done" % i)
		except:
			#print "not on matrix!"
			pass


def play(Input,x,y):
	text = Input
	length = len(text)

	for i in range(0, length*10+10):
		pixels = getChars(text,x,0)
		setMatrix(pixels)
		display()
		x = x -1

		time.sleep(0.025)
		clear()
	


Input = raw_input("Text to display: ").upper()
while True:
	clear()
	play(Input,10,0)
			
#abcdefghijklmnopqrstuvwxyz 1234567890.,:;-_+"@*#%&/()=?'^!$<>[]
