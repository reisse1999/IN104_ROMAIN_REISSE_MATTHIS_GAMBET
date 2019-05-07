import IN104_simulateur as simu
from MinimaxBrainAlphaBetaTime import MinimaxBrainABT
from randomBrain import RandomBrain

brain1 = RandomBrain()
human_time = 10 #the human will have 10 secs to play
brain2 = MinimaxBrainABT(simu.game.Game.defaultConfig, simu.game.Game.defaultRules)
game = simu.Game(brain1, human_time, brain2, brain2.time)
game.displayLevel = 1   # this prints the board after each move
game.runGame()
print(game.pdn) #print the summary of the game.

if(game.pdn != None):
    f=open('logs.txt','w')
    f.write(game.pdn)
    f.close()
