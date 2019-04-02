import IN104_simulateur as simu
from myAI import myAI

brain1 = myAI()
ai1_time = 1
brain2 = myAI()
ai2_time = 1
game = simu.Game(brain1, ai1_time, brain2, ai2_time)
game.displayLevel = 1   # this prints the board after each move
game.runGame()
print(game.pdn) #print the summary of the game. 

f=open('logs.txt','w')
f.write( game.pdn )
f.close()
