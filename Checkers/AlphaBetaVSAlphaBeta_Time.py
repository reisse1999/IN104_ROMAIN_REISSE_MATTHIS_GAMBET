import IN104_simulateur as simu
from MinimaxBrainAlphaBetaTime import MinimaxBrainABT
from MinimaxBrainAlphaBeta import MinimaxBrainAB
from game import Game

brain1 = MinimaxBrainABT(simu.game.Game.defaultConfig, simu.game.Game.defaultRules)
brain2 = MinimaxBrainAB()
ai_time = 10 #the AI will only have 1 sec to play
game = simu.Game(brain1, brain1.time, brain2, ai_time)
game.displayLevel = 1   # this prints the board after each move
game.runGame()
print(game.pdn) #print the summary of the game.

if(game.pdn != None):
    f=open('logs.txt','w')
    f.write(game.pdn)
    f.close()
