import IN104_simulateur as simu 
Cell = simu.Cell


def evaluate (gS):
	boardState = gS.boardState
	
	nber_black = 0
	nber_white = 0
	cells = boardState.cells
	for cell in cells :
		if Cell.isBlack(cell) :
			nber_black+=1
		if Cell.isWhite(cell):
			nber_white+=1
	return (nber_white - nber_black)

