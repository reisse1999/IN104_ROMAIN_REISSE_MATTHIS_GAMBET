import IN104_simulateur as simu
from evaluation import evaluate
from minimax_alphabeta import minimax
simu.GameState.get_children = simu.GameState.findNextStates
simu.GameState.evaluate = evaluate
import time

class MinimaxBrainAB:
    def __init__(self, config=None, rules=None):
        self.name = "MinimaxAlphaBetaBrain" # set your AI name here
        self.depth = 5 # Set the exploration depth here

    def play(self, gameState, timeLimit):
        #use minimax here to return the next state with higher score
        possibleStates = gameState.findNextStates()
        T = []
        max_T = -10000000000
        for state in possibleStates:
            if(minimax(state, self.depth, True) > max_T):
                chosen = state
            T.append(minimax(state, self.depth, True))
            max_T = max(T)
        return(chosen)


    def __str__(self):
        return self.name
