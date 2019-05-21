import IN104_simulateur as simu
from MinimaxBrainAlphaBetaTime import MinimaxBrainABT
from randomBrain import RandomBrain

brain1 = RandomBrain()
brain1_time = 1 #the human will have 10 secs to play
brain2 = MinimaxBrainABT(simu.game.Game.defaultConfig, simu.game.Game.defaultRules)
brain2_time = 0.5
game = simu.Game(brain1, brain1_time, brain2, brain2_time)
game.displayLevel = 1   # this prints the board after each move
game.runGame()
print(game.pdn) #print the summary of the game.

if(game.pdn != None):
    f=open('logs.txt','w')
    f.write(game.pdn)
    f.close()
