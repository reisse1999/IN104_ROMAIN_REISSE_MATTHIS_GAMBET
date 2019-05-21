import time
infinite = 10**10

def minimax(state, T, maximize, get_children, evaluate, delai, max_A = -infinite, min_A= infinite):
    start = time.time()
    if(maximize == True):
        maximize0 = False
    else:
        maximize0 = True
        
    children_list = get_children(state)
    length = len (children_list)
    if(length == 0):
        return(evaluate(state))
    G = []
    i = 0
    end = time.time()
    delay = end-start
    if(T-delay > delai):
        for child in children_list:
            end = time.time()
            delay = end-start
            Time_for_child = (T-delay)/length
            length= length-1

            if(len(G) != 0):
                G.append(minimax(child, Time_for_child, maximize0, get_children, evaluate, delai ,max(G), min(G)))
            else:
                G.append(minimax(child, Time_for_child, maximize0, get_children, evaluate, delai, -infinite, infinite))
            if(maximize == False):
                if(G[i] < max_A):
                    break
            else:
                if(G[i] > min_A):
                    break
            i += 1
            end = time.time()
            delay = end-start
            if(T-delay < delai):
                if(maximize == True):
                    res = max(G)
                    return(res)
                else:
                    res = min(G)
                    return(res) 
    else:
        return(evaluate(state))  
    if(maximize == True):
        return(max(G))
    else:
        return(min(G))
