import sys
import random
from .gameState import GameState

class RandomBrain:

    def __init__(self):
        print("Please enter your name")
        self.name = sys.stdin.readline()[0:-1]
        self.alwaysSeeAsWhite = False

    def play(self, gameState):
        possibleMoves = gameState.findPossibleMoves()
        print(gameState.toDisplay(True))
        list_moves = [m.toPDN() for m in possibleMoves]
        choice = random.choice(list_moves)
        return choice


    def __str__(self):
        return self.name
