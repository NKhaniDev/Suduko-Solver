#creat duduko table

def creat_sudoku_board():
    sudoku_board=[]

    for i in range(1,10):
        row=get_user_row_input(i)
        sudoku_board.append(row)
    return sudoku_board    


#getting row values from user

def get_user_row_input(index):

    user_input=input(f"enter {index} row")
    if len(user_input)==9 and user_input.isdigit():
        row_numbers=[]
        for char in user_input:
            row_numbers.append(int(char))
        print("|" + "|".join(user_input)+"|")
        return row_numbers
    else:
        print("invalid value")

#show sudko entered data

def display_sudoku(board):
    row_index=0
    for row in board:
        row_display="|"
        for num in row:
            if num==0:
                row_display += "  |"
            else:
                row_display+=str(num)+"  |  "
    
        print(row_display)
        row_index += 1 


# validation of user entered sudoku

def is_sudoku_valid(board):
    row_sets = []
    col_sets = []
    block_sets = []

    for _ in range(9):
        row_sets.append(set())
        col_sets.append(set())
        block_sets.append(set())

    for r in range(9):
        for c in range(9):
            num=board[r][c]
            if num !=0:
                block_index =(r//3)*3+(c//3)
                if num in row_sets[r] or num in col_sets[c] or block_sets[block_index]:
                    return False
                row_sets[r].add(num)
                col_sets[c].add(num)
                block_sets[block_index].add(num)

    return True         


# solving the puzzle

#find empty cells

def find_empty_spot(board):

    for row in range(9):
        for col in range(9):
            if board[row][col]==0:
                return row, col
                
    return None        

# check the cell feasibilty for adding the number

def can_place_number(board,num,row, col):
    for i in range(9):
        if board[row][i] == num:
            return False
        if board[i][col] == num:
            return False

    block_row_start=(row//3)*3
    block_col_start=(col//3)*3

    for i in range(3):
        for j in range(3):
            if board [block_row_start+i][block_col_start+j] == num:
                return False
            
    return True        


# solve puzzle
def solve_puzzle(board):

    empty_spot = find_empty_spot(board)
    if not empty_spot:
        return True
    r,c =empty_spot

    for number in range(1,10):
        if can_place_number(board,number.r,c):
            board[r][c]=number
            if solve_puzzle(board):
                return True
            board[r][c]=0
    return False        

# main solver
def run_sudoku_solver():
    while True:
        sudoku_board =creat_sudoku_board()
        print("current sudulu board")
        display_sudoku(sudoku_board)
        if is_sudoku_valid(sudoku_board):
            print("board is valid")

            if solve_puzzle(sudoku_board):
                print("Sudoku Solved.")
                display_sudoku(sudoku_board)
            else:
                print("No solution exist for the given Sudoku")  

        else:
            print("Board has conflicts and can not be solved.")

        if input("start from the begining?(y/n):").lower()  != "y":
            break    







#sudoku_board = creat_sudoku_board()
#display_sudoku(sudoku_board)

#if is_sudoku_valid(sudoku_board):
#    print("data ara correct")

#else:
#    print("data entered are not correct")

             
