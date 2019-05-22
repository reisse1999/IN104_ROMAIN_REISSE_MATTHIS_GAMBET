import IN104_simulateur as simu 
Cell = simu.Cell

def evaluate (gS):
	boardState = gS.boardState
	nber_black = 0
	nber_white = 0
	nberK_black = 0
	nberK_white = 0
	cells = boardState.cells
	for cell in cells :
		if Cell.isBlack(cell) :
			nber_black+=1
			if Cell.isKing(cell):
				nberK_black+=1
		if Cell.isWhite(cell):
			nber_white+=1
			if Cell.isKing(cell):
				nberK_white+=1
	return (nber_white - nber_black + 2*(nberK_white-nberK_black)) #une dame compte pour 3 pions (coefficient deux car les dames sont comptées aussi pour des pions)
