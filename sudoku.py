"""Python program using backtracking to solve sudokus"""

#________________Input________________________________________
"""Commented out are sudokus of various dificulties as shown respectively  
just comment the commented board and comment out another sample board to test the algorithm"""
"""The zeros on the board show empty boxes on the sudoku board"""

import time
start = time.time()
#standard
# board = [
#     [7,8,0,4,0,0,1,2,0],
#     [6,0,0,0,7,5,0,0,9],
#     [0,0,0,6,0,1,0,7,8],
#     [0,0,7,0,4,0,2,6,0],
#     [0,0,1,0,5,0,9,3,0],
#     [9,0,4,0,6,0,0,0,5],
#     [0,7,0,3,0,0,0,1,2],
#     [1,2,0,0,0,7,4,0,0],
#     [0,4,9,2,0,6,0,0,7]
# ]
#easy
# board = [
#     [5,3,0,0,7,0,0,0,0],
#     [6,0,0,1,9,5,0,0,0],
#     [0,9,8,0,0,0,0,6,0],
#     [8,0,0,0,6,0,0,0,3],
#     [4,0,0,8,0,3,0,0,1],
#     [7,0,0,0,2,0,0,0,6],
#     [0,6,0,0,0,0,2,8,0],
#     [0,0,0,4,1,9,0,0,5],
#     [0,0,0,0,8,0,0,7,9]
# ]
#expert
board = [
    [0,0,1,8,0,0,4,0,0],
    [4,6,0,0,0,0,0,0,0],
    [0,0,5,0,0,0,1,6,0],
    [0,0,0,0,3,0,0,8,7],
    [0,0,0,0,0,0,9,0,0],
    [3,0,0,9,1,0,0,5,0],
    [0,7,0,2,9,0,0,0,5],
    [0,0,3,0,0,0,0,0,0],
    [6,0,0,0,4,0,0,0,0]
]
#ridiculously_hard
# board = [
#     [0,0,0,4,0,0,0,0,0],
#     [0,0,0,0,0,8,0,9,6],
#     [0,0,0,0,5,3,0,8,0],
#     [0,4,8,0,0,0,0,0,0],
#     [2,0,0,0,4,9,0,0,1],
#     [6,0,0,0,0,0,5,0,9],
#     [4,0,0,1,0,0,7,0,0],
#     [0,8,0,9,0,0,4,0,0],
#     [0,1,0,0,7,0,0,2,0]
# ]

#hard
# board = [
#     [0,0,0,0,2,0,0,4,7],
#     [0,0,9,6,0,0,0,0,8],
#     [0,0,7,1,0,0,0,0,0],
#     [0,5,0,0,4,0,0,0,0],
#     [0,3,6,0,0,0,5,2,0],
#     [0,0,0,0,9,0,0,3,0],
#     [0,0,0,0,0,2,7,0,0],
#     [3,0,0,0,0,1,2,0,0],
#     [1,9,0,0,7,0,0,0,0]
# ]

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def show_board():#displays a formarted board
	count_num = 0
	count_row = 0
	count_strokes = 0
	column_div = 0
	print('\n')
	for row in board:
		count_row += 1
		for num in row:
			count_num += 1

			if count_num % 3 == 0:#creates columns
				print(num, end='   |   ')
			
				count_strokes += 1
				if count_strokes % 3 == 0:#creates rows
					print("\n")

					column_div += 1
					if column_div % 3 == 0:#divides rows in groups of 3
						print('---------------------------')			
				else:
					pass
			else:
				print(num, end='')

#show_board()

#=====================================================================================================

def isEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, column

    return None

#___________________________________________________________checks if the box is empty________________ 
def isValid(board, num, position):
    # Check row
    for i in range(len(board[0])):
        if board[position[0]][i] == num and position[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][position[1]] == num and position[0] != i:
            return False

    # Check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != position:
                return False

    return True

#__________________________________________________________BACKTRACKING ALGO_____________________________
def solver(board):
    find = isEmpty(board)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1,10):
        if isValid(board, i, (row, column)):
            board[row][column] = i

            if solver(board):
                return True

            board[row][column] = 0

    return False

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++___________output________________________________
show_board()#shows unsolved board
solver(board)#solves board
print("________________________________")
show_board()#shows the solved board
print("\nIt has taken " + str(time.time() - start) + " seconds to solve the Sudoku\n" )