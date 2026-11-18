#Step 6: detect a tie


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

winning_lines = [
    ['a1', 'a2', 'a3'],   # rows
    ['b1', 'b2', 'b3'],
    ['c1', 'c2', 'c3'],
    ['a1', 'b1', 'c1'],   # columns
    ['a2', 'b2', 'c2'],
    ['a3', 'b3', 'c3'],
    ['a1', 'b2', 'c3'],   # diagonals
    ['a3', 'b2', 'c1'],
]
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


def is_winner(turn,board):

    for line in winning_lines:
        chance = 0
        for l in line: 
            if board[l] == turn:
                chance +=1
            
        if chance == 3:
            return True
            
    return False


def is_tie(board):
    for i in board.values():
        if i == ' ':
            return False

    return True


print(print_board(board))
turn = 'X'

while True:
    response = input(f'{turn}, Pick a square: ')
    is_valid_response = reject_bad_input(response)
    if not is_valid_response:
        continue
    board[response] = turn
        
    print(print_board(board))
    is_check_winner = is_winner(turn,board)
    if is_check_winner:
        print (f'{turn}!! You are the winner')
        break
    if is_tie(board):
        print ("It's a TIE!")
        break



            


    
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    
        
