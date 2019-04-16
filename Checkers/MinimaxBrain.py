import IN104_simulateur as simu
from evaluation import evaluate
from minimax import minimax
simu.GameState.get_children = simu.GameState.findNextStates
simu.GameState.evaluate = evaluate

class MinimaxBrain:
    def __init__(self, config=None, rules=None):
        self.name = "Hello" # set your AI name here
        self.depth = 5 # Set the exploration depth here

    def play(self, gameState, timeLimit):
        #use minimax here to return the next state with higher score
        possibleStates = gameState.findNextStates()
        T = []
        for state in possibleStates:
            T.append(minimax(state, self.depth, True))
        return(max(T))

    def __str__(self):
        return self.name
