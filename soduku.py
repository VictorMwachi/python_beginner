def find_next_empty(puzzle):
    #find the next row,col in the puzzle that is not filled yet  ---> rep with -1
    #return  row,col tuple or none none if there is nothing to fill
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]=-1:
                return r,c
    return None,None # if no space in the puzle are empty

def is_valid(puzzle,guess,row,col):
    #determines if the guess is valid in the current row/col
    #returns false or true
    
    #start with row
    row_vals=puzzle[row]
    if guess in row_vals:
        False
    #then column
    col_vals=puzzle[i][col] for i in range(9)
    if guess in col_vals:
        False

    #then the square
    # get where 3x3 starts
    #and iterate over the three values in row and column

    row_start=(row//3)*3
    col_start=(col//3)*3

    for r in range(row_start,row_start+3):
        for c in range(col_start,col_start+3):
            if puzzle[i][c]==guess:
                return False

    # if pass this check

    return True


def soduku_solver(puzzle):
    # use backtracking method to solve soduku
    # our puzzle is a list of list where each inner list ia a row in our puzzle
    # return whether solution exists
    # mutates puzzle to be the solution(if solution exists)

    # step 1 choose somwhere on puzzle to make a guess

    row,col =find_next_empty(puzzle)

    #validate our guess

    if row is None:
        return True


    # step 2if there is a place to put a number hen make gues betwen 1 and 9
    for guess in range(1,10):
        #chek if this is a valid guess
        if is_valid(puzzle,guess,row,col):
            #if this is valid the put that guess in the puzzle

            puzzle[row][col]=guess
            # now recurse using this puzzle
            #step 4 recursively call our function

            if solve_soduku(puzzle):
                return True

            #step 5 if our guess is not valid or does not solve the puzzle then we need to
            #back track and try a new number

            puzzle[row][col]=-1

#if none of the numbers we try works then this puzzle is unsolvable
return False

example_board=[
    [3,9,-1,   -1,5,-1,   -1,-1,-1],
    [-1,-1,-1,   2,-1,-1,  -1,-1,5],
    [-1,-1,-1,  7,1,9, -1,8,-1],


    [-1,5,-1,  1,5,9, -1,-1,-1],
    [2,-1,6, -1,-1,3, -1,-1,-1],
    [-1,-1,-1, -1,-1,-1, -1,-1,4],

    [5,-1,-1, -1,-1,-1, -1,-1,-1],
    [6,7,-1 1,-1,5 -1,4,-1],
    [1,-1,9, -1,-1,-1, 2,-1,-1],

    
]

print(solve_soduku(example_board))
print(example_board)