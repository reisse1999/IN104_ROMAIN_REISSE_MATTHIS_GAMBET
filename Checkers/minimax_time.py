import time
from MinimaxBrainAlphaBetaTime import MinimaxBrainABT

brain = MinimaxBrainABT()
delai = brain.delai


def minimax_f(state, T, maximize, max_A, min_A):
    start = time.time()
    if(maximize == True):
        maximize0 = False
    else:
        maximize0 = True
        
    children_list = state.get_children()    
    if(len(children_list) == 0):
        return(state.evaluate())
    G = []
    explo = 1
    i = 0
    end = time.time()
    delay = end-start
    if(T-delay > delai):
        for children in children_list:
            if(explo == 1):
                if(len(G) != 0):
                    G.append(minimax_f(children, T-delay, maximize0, max(G), min(G)))
                else:
                    G.append(minimax_f(children, T-delay, maximize0, -1000000000, 1000000000))
                if(maximize == False):
                    if(G[i] < max_A):
                        explo = 0
                else:
                    if(G[i] > min_A):
                        explo = 0
                i += 1
                end = time.time()
                delay = end-start
                if(T-delay < delai):
                    if(maximize == True):
                        return(max(A))
                    else:
                        return(min(A)) 
    else:
        return(state.evaluate())  
    if(maximize == True):
        return(max(G))
    else:
        return(min(G))


def minimax(state, T, maximize):
    start = time.time()
    if(maximize == True):
        maximize0 = False
    else:
        maximize0 = True
    A = []
    end = time.time()
    delay = end-start
    if(T-delay > delai):
        for children in state.get_children():
            if(len(A) != 0):
                A.append(minimax_f(children, T-delay-delai, maximize0, max(A), min(A)))
            else:
                A.append(minimax_f(children, T-delay-delai, maximize0, -1000000000, 1000000000))
            end = time.time()
            delay = end-start
            if(T-delay < delai):
                if(maximize == True):
                    return(max(A))
                else:
                    return(min(A))   
    else:
        return(state.evaluate())  
    if(maximize == True):
        return(max(A))
    else:
        return(min(A))
        
