import time
import random
import math

class Board(object):
    """An N-queens solution attempt."""

    def __init__(self, queens):
        """Instances differ by their queen placements."""
        self.queens = queens.copy()

    def __len__(self):
        return len(self.queens)

    def display(self):
        """Print the board."""
        for r in range(len(self.queens)):
            for c in range(len(self.queens)):
                if self.queens[c] == r:
                    print ('Q', end=" ")
                else:
                    print ('Q', end=" ")
            print ()
        print ()

    def moves(self):
        """Return a list of possible moves given the current placements."""
        bestMoves = []
        optimalHeuristic = heuristic(board)
        for a, b in moves.iteritems():
            if b < optimalHeuristic:
                optimalHeuristic = b

        for a, b in moves.iteritems():
            if b == optimalHeuristic:
                bestMoves.append(a)

        return bestMoves

    def neighbor(self, move):
        """Return a Board instance like this one but with one move made."""
        if len(bestMoves) > 0:
            pick = random.randint(0, len(bestMoves) - 1)
            column = bestMoves[pick][0]
            row = bestMoves[pick][1]
            board[column] = row
        return board

    def heuristic(self):
        """Compute the cost of this solution."""
        h = 0
        ##checking columns
        for i in range(1, n):
            ##checking rows
            for j in range(i+1, n):
                if board[i] == board[j]:
                    h += 1
                x = j - i
                ##checking the diagonals
                if board[i] == board[j] - x or board[i] == board[j] + x:
                    h += 1
        return h

class Agent(object):
    """Knows how to solve an n-queens problem with simulated annealing."""

    def anneal(self, board):
        """Return a list of moves to adjust queen placements."""
        temperature = len(board)**2
        annealRate = 0.95
        newHeuristic = Board().heuristic()

        while newHeuristic > 0:
            board = makeMove(board, newHeuristic, temperature)
            newHeuristic = heuristic(board)
            newTemperature = max(temperature * annealRate, 0.01)
            temperature = newTemperature
            ##steps cap is here to avoid the algorithm getting stuck
            if steps >= 10000: 
                break

        boardCopy = list(board)
        foundMove = False

        while not foundMove:
            boardCopy = list(board)
            newRow = random.randint(0, len(board)-1)
            newColumn = random.randint(0, len(board)-1)
            boardCopy[newColumn] = newRow
            newHeuristic = heuristic(boardCopy)
            if newHeuristic < optimalHeuristic:
                foundMove = True
            else:
                delta_e = optimalHeuristic - newHeuristic
                ##aceptance prob equation min(1, e**(delta e/temp))
                acceptProbability = min(1, math.exp(delta_e/temperature))
                foundMove = random.random() <= acceptProbability
        return boardCopy

def main():
    """Create a problem, solve it with simulated anealing, and console-animate."""
    print("Enter the number of queens")
    n = int(input())
    queens = dict()
    for column in range(n):
        row = random.choice(range(n))
        queens[column] = row

    board = Board(queens)
    board.display()

    agent = Agent()
    path = agent.anneal(board)

    while path:
        move = path.pop(0)
        board = board.neighbor(move)
        time.sleep(0.1)
        board.display()

if __name__ == '__main__':
    main()