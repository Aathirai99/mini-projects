#Step 4: reject bad input


starting_board= """ 
{}|{}|{}
-+-+-
{}|{}|{}
-+-+-
{}|{}|{}
 """

board = {'a1': ' ', 'a2': ' ', 'a3': ' ',
         'b1': ' ', 'b2': ' ', 'b3': ' ',
         'c1': ' ', 'c2': ' ', 'c3': ' '}

def print_board(boards):
    squares = []
    for y in "abc":
        for x in '123':
            con = y+x
            
            val = boards[con]
            squares.append(val)
            

    return starting_board.format(*squares)

def reject_bad_input(square):
    if square in board.keys() and board[square]== ' ':
        return True
    else:
        return False

print(print_board(board))
turn = 'X'

while True:
    response = input(f'{turn}, Pick a square: ')
    is_valid_response = reject_bad_input(response)
    if not is_valid_response:
        continue
    board[response] = turn
        
    print(print_board(board))
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    
        
