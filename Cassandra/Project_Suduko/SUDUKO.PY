# def find_unassigned(arr, row, col):
#     for i in range(9):
#         for j in range(9):
#             if (arr[i][j] == 0):
#                 row = i
#                 col = j
#                 return True
#     return False
#
#
# def is_safe(
#         arr1,
#         num,
#         row,
#         col,
# ):
#     return not in_row(arr1, row, num) and not in_col(arr1, col, num) and not in_grid(arr1, row - row % 3, col - col % 3,
#                                                                                      num)  # current column and current 3x3 box
#
#
# def in_row(arr2, row, num):
#     for i in range(9):
#         if arr2[row][i] == num:
#             return True
#     return False
#
#
# def in_col(arr3, col, num):
#     for i in range(9):
#         if arr3[i][col] == num:
#             return True
#     return False
#
#
# def in_grid(
#         arr4,
#         row,
#         col,
#         num,
# ):
#     for i in range(3):
#         for j in range(3):
#             if (arr4[i + row][j + col] == num):
#                 return True
#     return False
#
#
# def print_grid(arr5):
#     for i in range(9):
#         for j in range(9):
#             print(arr5[i][j], end=" ")
#         print()
#
#
# def solve_sudoku(arr6):
#     row = col = 0
#     if not find_unassigned(arr6, row, col):
#         return True
#     for num in range(1, 10):
#         if is_safe(arr6, num, row, col):
#             arr6[row][col] = num
#             if solve_sudoku(arr6):
#                 return True
#             arr6[row][col] = 0
#     return False
#
#
# # Driver main function
#
# if __name__ == '__main__':
#
#     # creating a 2D array
#
#     grid = [[0 for x in range(9)] for y in range(9)]
#
#     # assigning values to the grid
#
#     grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
#             [5, 2, 0, 0, 0, 0, 0, 0, 0],
#             [0, 8, 7, 0, 0, 0, 0, 3, 1],
#             [0, 0, 3, 0, 1, 0, 0, 8, 0],
#             [9, 0, 0, 8, 6, 3, 0, 0, 5],
#             [0, 5, 0, 0, 9, 0, 6, 0, 0],
#             [1, 3, 0, 0, 0, 0, 2, 5, 0],
#             [0, 0, 0, 0, 0, 0, 0, 7, 4],
#             [0, 0, 5, 2, 0, 6, 3, 0, 0]]
#
#     # if success print the grid
#
#     if solve_sudoku(grid):
#         print_grid(grid)
#     else:
#         print("No solution exists")

# def solve_sudoku(grid):
# 	row=col=0
# 	if(not find_unassigned(grid,row,col)):
# 		return True
# 	for num in range(1,10):
# 		if(is_safe(grid,num,row,col)):
# 			grid[row][col]=num
# 			if(solve_sudoku(grid)):
# 				return true
# 		grid[row][col] = 0
# 	return False
#
#
# def find_unassigned(grid,row,col):
# 	for i in range(9):
# 		for j in range(9):
# 			if(grid[i][j]==0):
# 				row=i
# 				col=j
# 				return True
# 	return False
#
# def is_safe(grid,num,row,col):
# 	 return not in_row(grid,row,num) and not in_col(grid,col,num) and not in_grid(grid,row-row%3,col-col%3,num)# current column and current 3x3 box
#
# def in_row(grid,row,num):
#  	for i in range(9):
# 		if grid[row][i]==num:
# 			return True
#  	return False
#
# def in_col(grid,col,num):
#  	for i in range(9):
# 		if(grid[i][col]==num):
# 			return True
#  	return False
#
# def in_grid(grid,row,col,num):
#  	for i in range(3):
# 		for j in range(3):
# 			if(grid[i+row][j+col]==num):
# 				return True
#  	return False
#
# def print_grid(grid):
#  for i in range(9):
#   for j in range(9):
#    print(grid[i][j]),
#   print()
#
# # Driver main function
# if __name__=="__main__":
# 	# creating a 2D array
# 	grid=[[0 for x in range(9)]for y in range(9)]
#
# 	# assigning values to the grid
#  grid=[[3,0,6,5,0,8,4,0,0],
# 	  [5,2,0,0,0,0,0,0,0],
# 	  [0,8,7,0,0,0,0,3,1],
# 	  [0,0,3,0,1,0,0,8,0],
# 	  [9,0,0,8,6,3,0,0,5],
# 	  [0,5,0,0,9,0,6,0,0],
# 	  [1,3,0,0,0,0,2,5,0],
# 	  [0,0,0,0,0,0,0,7,4],
# 	  [0,0,5,2,0,6,3,0,0]]
#
# 	# if success print the grid
#  if solve_sudoku(grid):
#   print_grid(grid)
#  else:
#   print "No solution exists"


# A Backtracking program in Python to solve Sudoku problem


# A Utility Function to print the Grid
def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" ")
        print()


# Function to Find the entry in the Grid that is still not used
# Searches the grid to find an entry that is still unassigned. If
# found, the reference parameters row, col will be set the location
# that is unassigned, and true is returned. If no unassigned entries
# remain, false is returned.
# 'l' is a list variable that has been passed from the solve_sudoku function
# to keep track of incrementation of Rows and Columns
def find_empty_location(arr, l):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False


# Returns a boolean which indicates whether any assigned entry
# in the specified row matches the given number.
def used_in_row(arr, row, num):
    for i in range(9):
        if arr[row][i] == num:
            return True
    return False


# Returns a boolean which indicates whether any assigned entry
# in the specified column matches the given number.
def used_in_col(arr, col, num):
    for i in range(9):
        if arr[i][col] == num:
            return True
    return False


# Returns a boolean which indicates whether any assigned entry
# within the specified 3x3 box matches the given number
def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[i + row][j + col] == num:
                return True
    return False


# Checks whether it will be legal to assign num to the given row,col
# Returns a boolean which indicates whether it will be legal to assign
# num to the given row,col location.
def check_location_is_safe(arr, row, col, num):
    # Check if 'num' is not already placed in current row,
    # current column and current 3x3 box
    return not used_in_row(arr, row, num) and not used_in_col(arr, col, num) and not used_in_box(arr, row - row % 3,
                                                                                                 col - col % 3, num)


# Takes a partially filled-in grid and attempts to assign values to
# all unassigned locations in such a way to meet the requirements
# for Sudoku solution (non-duplication across rows, columns, and boxes)
def solve_sudoku(arr):
    # 'l' is a list variable that keeps the record of row and col in find_empty_location Function
    l = [0, 0]

    # If there is no unassigned location, we are done
    if not find_empty_location(arr, l):
        return True

    # Assigning list values to row and col that we got from the above Function
    row = l[0]
    col = l[1]

    # consider digits 1 to 9
    for num in range(1, 10):

        # if looks promising
        if check_location_is_safe(arr, row, col, num):

            # make tentative assignment
            arr[row][col] = num

            # return, if success, ya!
            if solve_sudoku(arr):
                return True

            # failure, unmake & try again
            arr[row][col] = 0

    # this triggers backtracking
    return False


# Driver main function to test above functions
if __name__ == "__main__":

    # creating a 2D array for the grid
    grid = [[0 for x in range(9)] for y in range(9)]

    # assigning values to the grid
    grid = [[0, 0, 4, 0, 0, 0, 1, 7, 0],
            [9, 0, 0, 0, 0, 7, 6, 0, 0],
            [7, 3, 0, 0, 0, 0, 4, 0, 0],
            [3, 0, 0, 9, 7, 0, 0, 0, 0],
            [0, 8, 9, 3, 0, 0, 0, 0, 2],
            [0, 0, 6, 0, 8, 4, 0, 9, 0],
            [0, 2, 0, 0, 0, 0, 9, 6, 7],
            [0, 0, 0, 0, 3, 6, 0, 0, 1],
            [0, 0, 0, 2, 0, 0, 0, 0, 0]]

    # if success print the grid
    if solve_sudoku(grid):
        print_grid(grid)
    else:
        print("No solution exists")

# The above code has been contributed by Harshit Sidhwa.
