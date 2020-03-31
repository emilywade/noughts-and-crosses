# Noughts & Crosses
# Introduction

Game theory is involved in Artificial Intelligence (AI) whenever
multi-agent situations arise in which more than one person has to make
logical decisions. Whilst the number of game theory applications in this
field covers a wide variety of topics, by far the most common
application is within digital games. In this report we will consider the
use of AI in the popular two-player game Noughts & Crosses.

# Noughts & Crosses

Noughts & Crosses is a zero-sum, sequential game with perfect
information. It is typically played on a 3x3 grid, with one player
acting as ‘O’ and the other acting as ‘X’. The winner is the first
player to place three of their marks in a horizontal, vertical or
diagonal row. The payoff functions for each player are
\(u:states \rightarrow \mathbb{R}\), where the strategy space is the set
of all possible board configurations (or states) at any given time.

Through the use of AI, Noughts & Crosses can be played as a
single-player game by teaching the computer a ’best strategy’ for any
given board configuration. In order to do this we must consider the game
tree; a recursive search function which examines each ply (move) and its
associated game result.

The state-space complexity of a game is the set of all legal game states
branching from the intitial state. In Noughts & Crosses, the initial
state is an empty board, and a move is legal given that the square is
currently empty. This gives us the state-space complexity upper bound of
\(3^9 = 19,683\), since there are three states for each of the nine
squares. However, this calculation includes many illegal moves,
including five noughts and zero crosses, and so it is apparent from the
offset that there exist simplifications to our game tree exploration. We
will see that it is possible to use this game tree alongside other tools
to develop an optimal game strategy.

# Minimax Algorithm

## Definition

A natural choice for optimal decision making in game theory and
artificial intelligence is the recursive Minimax algorithm. It assigns
two players, MIN and MAX, who work against each other. The MAX player
tries to obtain the highest score possible, and MIN acts as a helper to
MAX by trying to obtain the lowest score possible.

## Algorithm Procedure

1.  Generate the complete game tree, consisting of:
    
      - Initial state: the blank board configuration showing whose move
        it is.
    
      - Successor functions: comprises all legal moves available to the
        player.
    
      - Terminal state: shows the board configuration for the MAX player
        when the game terminates (either win, lose or draw).
    
      - Utility function: assigns numeric value to the game outcome,
        namely -1 for a loss, 0 for a tie and +1 for a win.

2.  Apply the utility function to the terminal states.

3.  Calculate the utilities of higher nodes. A MAX node calculates the
    maximum of its child nodes, and a MIN node calculates the minimum.

4.  When the utility value reaches the initial state, choose the maximum
    value to determine the MAX player’s corresponding move.

This process is called the Minimax decision; it maximises the utility
assuming that the opponent is also playing optimally to minimse it.

![Applying Algorithm](minimax-def.png)

![Determining Utilities](utilities-minimax.jpg)

## Alpha-Beta Pruning

It is possible to improve upon this simple algorithm by applying a
number of different heuristics. These are helpful rules which act as a
guidance in decision making and effectively allow us to ‘prune’ a
decision tree. One useful heuristic in this game is known as Alpha–Beta
pruning. This optimisation technique stops evaluating a move when it is
worse than a previously known move. We require two extra values be
retained throughout the decision making process:

  - Alpha value: best previously known move for the MAX player

  - Beta value: best previously known move for the MIN player

We eliminate game tree paths when its alpha value is greater than or
equal to its beta value.

By implementing this optimisation into the Minimax algorithm we obtain
the same result, but since we no longer need to search the entire game
tree before each ply made, the time to make each decision is
dramatically improved.

## Python Implementation

We begin by defining basic game functions in a ‘class’ statement,
comprising the initial board configuration, a way of checking a given
ply is legal and a way of checking if a ply has ended the game.

We then implement our Minimax function. We first define our MAX player,
who seeks to maximise their utility function, and then we define our MIN
player, who will help our AI to minimise their losses.

    def max_alpha_beta(self, alpha, beta):
            maxv = 0
            px = None
            py = None
    
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
                        self.current_state[i][j] = 'O'
                        (m, min_i, in_j) = self.min_alpha_beta(alpha, beta)
                        if m > maxv:
                            maxv = m
                            px = i
                            py = j
                        self.current_state[i][j] = '.'
    
                        if maxv >= beta:
                            return (maxv, px, py)
    
                        if maxv > alpha:
                            alpha = maxv
    
            return (maxv, px, py)

    def min_alpha_beta(self, alpha, beta):
            minv = 0
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
                        (m, min_i, in_j) = self.max_alpha_beta(alpha, beta)
                        if m > minv:
                            minv = m
                            qx = i
                            qy = j
                        self.current_state[i][j] = '.'
    
                        if minv <= alpha:
                            return (minv, qx, qy)
    
                        if minv < beta:
                            beta = minv
    
            return (minv, qx, qy)
            
We can then set up a game loop calling to each of these functions, and
finally initialise the game. This algorithm ensures that the opponent
will at best draw, and if they do not play optimally then they will
lose.

By importing the time module into our script and recording the average
time taken to calculate MAX’s first move, both with and without pruning,
we can see a 99.28% decrease in evaluation time when using this
optimisation technique:

|        **Method**        | **Avg Evaluation Time (s) (4sf)** |  |
| :----------------------: | :-------------------------------: | :-: |
| Simple Minimax Algorithm |               7.584               |  |
| Added Alpha-Beat Pruning |              0.05430              |  |

# Conclusion

The use of the Minimax algorithm is an effective way to implement AI
into two-player games. The simple, recursive algorithm allows us to
create an AI that is impossible to beat in Noughts & Crosses.
Introducing Alpha-Beta Pruning to this provides a much more elegant
algorithm, dramatically decreasing evaluation time and speeding up the
game for the opponent.

<span>9</span> Scratch: Game Tree.  
`https://en.scratch-wiki.info/wiki/Game_Tree`

Wikipedia: Game Complexity.  
`https://en.wikipedia.org/wiki/Game_complexity`

R Jain: Minimax Algorithm with Alpha-beta pruning,  
`https://www.hackerearth.com/blog/developers/minimax-algorithm-alpha-beta-pruning`

A A. Elnaggar, M Gadallah, M A Aziem, H El-Deeb. *A Comparative Study of
Game Tree Searching Methods*. \[*IJACSA*.\] Vol. 5, No. 5, 2014.

M Krivokuća: Minimax with Alpha-Beta Pruning in Python  
`https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/`
