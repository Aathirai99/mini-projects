# Create the empty board and print it
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


print(print_board(board))



board['b2'] = 'X'