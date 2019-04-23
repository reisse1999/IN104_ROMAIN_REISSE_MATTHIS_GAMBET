






def minimax (state, max_depth, maximize ,transposition_table={}) :
	
	if max_depth == 0:
		return state.evaluate()

	

	children_list = state.get_children()
	if len(children_list) ==0:
		return state.evaluate()

	if state in transposition_table :
		return transposition_table [state]

	if maximize :
		score_ref = -1000000000000000
	else:
		score_ref =  1000000000000000




	for node in children_list:
		score = minimax(node, max_depth-1, bool ( (maximize+1)%2 ) )

		if maximize :
			if score > score_ref:
				score_ref = score

		else :
			if score < score_ref:
				score_ref = score



	transposition_table[state] = score_ref
	return score_ref
