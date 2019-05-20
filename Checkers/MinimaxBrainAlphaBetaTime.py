import IN104_simulateur as simu
from evaluation import evaluate
from minimax_time import minimax
simu.GameState.get_children = simu.GameState.findNextStates
simu.GameState.evaluate = evaluate
import time

class MinimaxBrainABT:
    def __init__(self, config, rules):
        self.name = "MinimaxAlphaBetaBrainTime" # set your AI name here
        self.time = 1
        Etat = simu.GameState(config, rules)
        debut = time.time()
        Etat_suivant = Etat.findNextStates()
        fin = time.time()
        self.delai = fin - debut

    def play(self, gameState, timeLimit):
        #use minimax here to return the next state with higher score
        possibleStates = gameState.findNextStates()
        T = []
        max_T = -10000000000
        n = len(possibleStates)
        temps_T = (self.time)-(self.delai)
        temps = (temps_T)/(n)
        i = 0
        for state in possibleStates:
            debut = time.time()
            Mini = minimax(state, temps, True, self.delai)
            if(Mini > max_T):
                chosen = state
            T.append(Mini)
            max_T = max(T)
            fin = time.time()
            temps_T -= (fin-debut)
            i += 1
            if(i != n):
                temps = (temps_T)/(n-i)
        return(chosen)


    def __str__(self):
        return self.name
