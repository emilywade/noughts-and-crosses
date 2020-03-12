
# coding: utf-8

# In[ ]:

# Tic Tac Toe game

# creating a board
board = [' ' for x in range(10)]

# insertletter function takes 2 parameters; inserts given letter at given position
def insertLetter(letter, pos):
    board[pos] = letter

# spaceisfree function tells us if space is free or not    
def spaceIsFree(pos):
    return board[pos] == ' '

# printboard function takes board as paramenter and displays to console 
def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

# iswinner function tells us if the given letter has won based on the current board; two parameters board and letter    
def isWinner(bo, le):
    return
    (bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[1] == le and bo[4] == le and bo[7] == le) or
    (bo[2] == le and bo[5] == le and bo[8] == le) or
    (bo[3] == le and bo[6] == le and bo[9] == le) or
    (bo[1] == le and bo[5] == le and bo[9] == le) or
    (bo[3] == le and bo[5] == le and bo[7] == le)

# ask user to input a move and validate    
def playerMove():
    run = True
    while run: # keep looping until we get a valid move
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10: # make sure we type a number from 1-9
                if spaceIsFree(move): # check no other letter is there already
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
            
# AI - examines board and makes best move possible
#ALGORITHM:
#1. if there is a winning move, take it
#2. if player has winning move on next turn, take it.
#3. take any of corners. randomly decide if more than one avail.
#4. take center pos.
#5. take one of edges. randomly decide if more than one avail.
#6. no move poss then game is a tie.
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0] # create list of possible moves
    move = 0
    
    # check for possible winning move to take or to block opponents winning move
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move
    
    # try to take a corner
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move
    
    # try to take center
    if 5 in possibleMoves:
        move = 5
        return move
    
    # try to take an edge
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move

# randomly decides on a move to take given a list of possible positions
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    
# returns true if board is full and false if not
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

# main game loop
def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')

# initalise the game
while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break


# In[ ]:



