import time

def minimax_f(state, T, maximize, max_A, min_A, delai):
    start = time.time()
    if(maximize == True):
        maximize0 = False
    else:
        maximize0 = True
        
    children_list = state.get_children()
    length = len (children_list)
    if(length== 0):
        return(state.evaluate())
    G = []
    explo = 1
    i = 0
    end = time.time()
    delay = end-start
    if(T-delay > delai):
        for child in children_list:
            end = time.time()
            delay = end-start
            Time_for_child = (T-delay)/length
            length= length-1
            if(explo == 1):
                if(len(G) != 0):
                    G.append(minimax_f(child, Time_for_child, maximize0, max(G), min(G), delai))
                else:
                    G.append(minimax_f(child, Time_for_child, maximize0, -1000000000, 1000000000, delai))
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
                        return(max(G))
                    else:
                        return(min(G)) 
    else:
        return(state.evaluate())  
    if(maximize == True):
        return(max(G))
    else:
        return(min(G))


def minimax(state, T, maximize, delai):
    start = time.time()
    if(maximize == True):
        maximize0 = False
    else:
        maximize0 = True
    A = []
    children_list = state.get_children()
    end = time.time()
    delay = end-start  
    length = len(children_list)
    if(length == 0):
        return(state.evaluate())
    if(T -delay> delai):
        for child in children_list:
            end = time.time()
            delay = end-start
            Time_for_child = (T-delay) / length
            length = length -1
            if(len(A) != 0):
                A.append(minimax_f(child, Time_for_child, maximize0, max(A), min(A), delai))
            else:
                A.append(minimax_f(child, Time_for_child, maximize0, -1000000000, 1000000000, delai))
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
