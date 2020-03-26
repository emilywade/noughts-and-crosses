
# coding: utf-8

# In[ ]:

#NOUGHTS AND CROSSES MINIMAX ALGORITHM

import time # to quantify difference between simple minimax and optimised methods

# definitions to form game
class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]

        # player X to play first
        self.player_turn = 'X'

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

    # determines if the move is legal
    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2: # must be on the board
            return False
        elif self.current_state[px][py] != '.': # must be currently empty
            return False
        else:
            return True
        
    # checks if the game has ended and returns the winner if it has
    def is_end(self):
        # vertical win
        for i in range(0, 3):
            if (self.current_state[0][i] != '.' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        # horizontal win
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                return 'O'

        # diagonal win
        if (self.current_state[0][0] != '.' and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        # diagonal win
        if (self.current_state[0][2] != '.' and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

        # check if board is full
        for i in range(0, 3):
            for j in range(0, 3):
                # if there's an empty field game continues
                if (self.current_state[i][j] == '.'):
                    return None

        # it's a tie
        return '.'
    
    # AI player 'O' is MAX
    def max(self):
        # initially set utility to 0
        maxv = 0

        px = None
        py = None

        result = self.is_end()

        # if game ends, return terminal state utility 
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    # on empty field comp makes move and calls MIN
                    self.current_state[i][j] = 'O'
                    (m, min_i, min_j) = self.min()
                    # fixing maxv value
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    # setting field back to empty    
                    self.current_state[i][j] = '.'
        return (maxv, px, py)
    
    # Human player 'X' is MIN
    def min(self):
        
        minv = 2

        qx = None
        qy = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.'

        return (minv, qx, qy)
    
    # game loop
    def play(self):
        while True:
            self.draw_board()
            self.result = self.is_end()

            # if game has ended
            if self.result != None:
                if self.result == 'X':
                    print('The winner is X!')
                elif self.result == 'O':
                    print('The winner is O!')
                elif self.result == '.':
                    print('It\'s a tie!')

                self.initialize_game()
                return

            # if it's player's turn
            if self.player_turn == 'X':

                while True:

                    start = time.time()
                    (m, qx, qy) = self.min()
                    end = time.time()
                    print('Evaluation time: {}s'.format(round(end - start, 7)))
                    
                    px = int(input('Insert the X coordinate: '))
                    py = int(input('Insert the Y coordinate: '))

                    (qx, qy) = (px, py)

                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('Invalid - try again.')

            # if it's AI's turn
            else:
                (m, px, py) = self.max()
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'


# In[ ]:

# begin game
def main():
    g = Game()
    g.play()

if __name__ == "__main__":
    main()


# In[ ]:



