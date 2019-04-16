def minimax(state, max_depth, maximize):
    depth = max_depth
    if(depth > 0):
        depth -= 1
        if(maximize == True):
            maximize0 = False
        else:
            maximize0 = True
        if(len(state.get_children()) == 0):
            return(state.evaluate())
        T = []
        for children in state.get_children():
            T.append(minimax(children, depth, maximize0))
        if(maximize == True):
            return(max(T))
        else:
            return(min(T))
        
    else:
        return(state.evaluate())
