

def creat_sudoku_board():
    """
    Collects the full sudoku table from the user.
    """
    sudoku_board=[]

    for i in range(1,10):
        row=get_user_row_input(i)
        if row == "exit":
            return "exit"
        
        sudoku_board.append(row)
    return sudoku_board    




def get_user_row_input(index):
    """
    request a row of numbers from the user.
    """

    while True:  

        user_input=input(f"Please enter {index} row:  \n")
        if user_input.lower() == 'exit':
             return "exit"
        if len(user_input)==9 and user_input.isdigit():
            valid_input = True
            row_numbers = []
            row_string = "|"
            for char in user_input:
                if '0' <= char <= '9':
                    row_numbers.append(int(char))
                    row_string+= char + "|"
                else:    
                    valid_input = False
                    break

            if valid_input:    
                print(row_string)

                return row_numbers
            else:
                print("Invalid value. Each digit must be between 1 and 9.\n")

        else:
            print("invalid value. Please ensure all characters are digits from 1 to 9 and exatly 9 long.\n")



def display_sudoku(board):
    """
    display the sudoku in a visually appealling format.
    """
    print("+--------------+---------------+---------------+")
    for i in range(len(board)):
        

        row_display="|"
        
        for j in range(len(board[i])):
            num = board[i][j]
            if num==0:
                row_display += "    |"
            else:
                row_display += f" {num:2} |"

            if (j + 1) % 3 == 0 and (j + 1) != 9:
                row_display += "|"

        print(row_display)
        
        if (i + 1) % 3 == 0:
            print("+--------------+---------------+---------------+")        





def is_sudoku_valid(board):
    """
    Check if the provided Sudoku board has any conflicts.
    """
    row_sets = []
    col_sets = []
    block_sets = []

    for _ in range(9):
        row_sets.append(set())
        col_sets.append(set())
        block_sets.append(set())

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num != 0:
                block_index =(r//3) * 3 + c//3
                if num in row_sets[r] or num in col_sets[c] or num in block_sets[block_index]:
                    return False
                row_sets[r].add(num)
                col_sets[c].add(num)
                block_sets[block_index].add(num)

    return True         




def find_empty_spot(board):
    """ 
    Find the next empty spot on the board.
    """

    for row in range(9):
        for col in range(9):
            if board[row][col]==0:
                return row, col
                
    return None        



def can_place_number(board,num,row, col):
    """ 
    Check if it's valid to place a number in a specific spot.
    """
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



def solve_puzzle(board):
    """ 
    Solve the Sudoku puzzle using a recursive backtracking algorithm.
    """
    empty_spot = find_empty_spot(board)
    if not empty_spot:
        return True
    r,c =empty_spot

    for number in range(1,10):
        if can_place_number(board,number,r,c):
            board[r][c]=number
            if solve_puzzle(board):
                return True
            board[r][c]=0
    return False        


def run_sudoku_solver():
    """ 
    The main function that runs the Sudoku solver program.
    """
    print("=======================================")
    print("             Sudoku Solver")
    print("=======================================")
    print("Welcome to the Interactive Sudoku Solver!")
    print("Instructions:")
    print("1. You will be prompted to enter each row of the Sudoku grid.")
    print("2. Each row must contain exactly 9 digits, where '0' represents an empty cell.")
    print("3. Enter the digits consecutively without spaces (e.g., 530470001 for the first row).")
    print("4. At any point, if you wish to exit, type 'exit' instead of entering a row.")
    print("5. After all rows are entered, the solver will attempt to solve the Sudoku if it's valid.")
    print("6. If the board has any conflicts or if an incorrect entry is made, you will be notified.")
    print("7. You can restart at any time by answering 'y' when asked to start from the beginning after solving or exiting.")
    print("\nLet's start entering the Sudoku grid!\n")

    while True:
        sudoku_board =creat_sudoku_board()
        if sudoku_board == "exit":
            print("Exiting solver.\n")
            break
        print("Current Sudoku board:\n")
        display_sudoku(sudoku_board)
        if is_sudoku_valid(sudoku_board):
            print("board is valid.\n")

            if solve_puzzle(sudoku_board):
                print("Sudoku Solved.\n")
                display_sudoku(sudoku_board)
            else:
                print("No solution exist for the given Sudoku.\n")  

        else:
            print("Board has conflicts and can not be solved.\n")

        if input("start from the begining?(y/n):  ").lower()  != "y":
            break    

if __name__=="__main__":
  run_sudoku_solver()







             
