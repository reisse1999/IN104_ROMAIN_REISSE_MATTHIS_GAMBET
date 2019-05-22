import IN104_simulateur as simu
from evaluation import evaluate
from minimax_time import minimax
import time

class MinimaxBrainABT:
    def __init__(self, config=None, rules=None):
        self.name = "MinimaxAlphaBetaBrainTime" # set your AI name here
        Etat = simu.GameState(config, rules)
        debut = time.time()
        Etat_suivant = Etat.findNextStates()
        fin = time.time()
        self.delai = fin - debut

    def play(self, gameState, timeLimit):
        #use minimax here to return the next state with higher score
        possibleStates = gameState.findNextStates()
        max_T = -10000000000
        n = len(possibleStates)
        temps_T = (timeLimit)-(self.delai)
        i = 0
        for state in possibleStates:
            temps = (temps_T)/(n-i)
            debut = time.time()
            Mini = minimax(state, temps, True, simu.GameState.findNextStates, evaluate, self.delai)
            if(Mini > max_T):
                chosen = state
                max_T = Mini
            fin = time.time()
            temps_T -= (fin-debut)
            i += 1
        return(chosen)


    def __str__(self):
        return self.name
