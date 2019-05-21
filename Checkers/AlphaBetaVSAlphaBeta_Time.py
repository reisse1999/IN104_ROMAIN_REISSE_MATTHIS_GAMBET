import IN104_simulateur as simu
from MinimaxBrainAlphaBetaTime import MinimaxBrainABT
from MinimaxBrainAlphaBeta import MinimaxBrainAB

brain1 = MinimaxBrainABT(simu.game.Game.defaultConfig, simu.game.Game.defaultRules)
brain1_time = 0.5
brain2 = MinimaxBrainAB()
brain2_time = 0.5 #the AI will only have 1 sec to play
game = simu.Game(brain1, brain1_time, brain2, brain2_time)
game.displayLevel = 1   # this prints the board after each move
game.runGame()
print(game.pdn) #print the summary of the game.

if(game.pdn != None):
    f=open('logs.txt','w')
    f.write(game.pdn)
    f.close()
