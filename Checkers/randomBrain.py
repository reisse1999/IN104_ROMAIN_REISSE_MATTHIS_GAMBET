import sys
import random
from .gameState import GameState
from .move import Move

class RandomBrain:

    def __init__(self):
        print("Please enter your name")
        self.name = sys.stdin.readline()[0:-1]
        self.alwaysSeeAsWhite = False

    def play(self, gameState, timeLimit):
        possibleMoves = gameState.findPossibleMoves()
        list_moves = [m.toPDN() for m in possibleMoves]
        string = random.choice(list_moves)
        move = Move.fromPDN(string)
        choice = gameState.doMove(move, inplace = False)
        return choice

    def __str__(self):
        return self.name
