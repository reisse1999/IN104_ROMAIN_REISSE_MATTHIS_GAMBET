import sys
import random
from IN104_simulateur.gameState import GameState
from IN104_simulateur.move import Move

class RandomBrain:

    def __init__(self):
        self.name = "RandomBrain"
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
