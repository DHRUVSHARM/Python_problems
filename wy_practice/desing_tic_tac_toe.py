"""
Docstring for wy_practice.desing_tic_tac_toe

Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

A move is guaranteed to be valid and is placed on an empty block.

Once a winning condition is reached, no more moves are allowed.

A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.


2 <= n <= 100 - imp

player is 1 or 2. - imp

0 <= row, col < n

(row, col) are unique for each different call to move.

At most n² calls will be made to move.


1 1 1 
1 1 1 
1 1 1


1 1
1 1


"""


class TicTacToe:

    def __init__(self, n: int):
        # 0 for unplaced, 1 , 2 for player
        self.grid = [[0 for _ in range(0 , n)] for _ in range(0 , n)]
        self.size = n # unchanged

    def state(self , x , y , player):
        # we want to check 
        dirs = [ [(-1 , 0) , (1 , 0)] , [(0 , -1) , (0 , 1)] , [(-1 , -1) , (1 , 1)] , [(-1 , 1) , (1 , -1)] ]
        
        for direction in dirs:
            count = 0
            for dx , dy in direction:
                newx , newy = x + dx , y + dy
                while 0 <= newx < self.size and 0 <= newy < self.size and self.grid[newx][newy] == player:
                    count += 1
                    newx += dx
                    newy += dy
            # we have count for one direction
            if (count + 1) == self.size:
                return player # won
        
        # still in progress
        return 0


    def move(self, row: int, col: int, player: int) -> int:
        # 0 - no winner game in progress
        # 1 - player 1 wins
        # 2 - player 2 wins
        # row col pos is unique it is 0 and in range
        if self.grid[row][col] != 0:
            raise Exception("Invalid move !!!")

        self.grid[row][col] = player

        # we need to write an effecient function to check winning 
        return self.state(row , col , player)        



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
