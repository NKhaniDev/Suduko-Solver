#creat duduko table

def creat_sudoku_board():
    sudoku_board=[]

    for i in range(1,10):
        row=get_user_row_input(i)
        sudolu_board.append(row)
    return sudoku_board    


#geeting row values from user

def get_user_row_input(index):

    user_input=input(f"enter {index} row")
    if len(user_input)==9 and user_input.indigit():
        row_numbers=[]
        for char in user_input:
            row_numbers.append(int(char))
        print(join(user_input))
        return row_numbers
    else:
        print("invalid value")


creat_sudoku_board() 