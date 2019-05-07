def minimax_f(state, max_depth, maximize, max_T, min_T):
    depth = max_depth
    if(depth > 0):
        depth -= 1
        if(maximize == True):
            maximize0 = False
        else:
            maximize0 = True
        if(len(state.get_children()) == 0):
            return(state.evaluate())
        G = []
        explo = 1
        i = 0
        for children in state.get_children():
            if(explo == 1):
                if(len(G) != 0):
                    G.append(minimax_f(children, depth, maximize0, max(G), min(G)))
                else:
                    G.append(minimax_f(children, depth, maximize0, -1000000000, 1000000000))
                if(maximize == False):
                    if(G[i] < max_T):
                        explo = 0
                else:
                    if(G[i] > min_T):
                        explo = 0
                i += 1  
        if(maximize == True):
            return(max(G))
        else:
            return(min(G))
        
    else:
        return(state.evaluate())

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
        explo = 1
        i = 0
        for children in state.get_children():
            if(len(T) != 0):
                T.append(minimax_f(children, depth, maximize0, max(T), min(T)))
            else:
                T.append(minimax_f(children, depth, maximize0, -1000000000, 1000000000)) 
        if(maximize == True):
            return(max(T))
        else:
            return(min(T))
        
    else:
        return(state.evaluate())
