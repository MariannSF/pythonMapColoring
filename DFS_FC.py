from datetime import datetime
import CFS as cfs
import DFS as dfs
import DFS_FC as fc
import DFS_FC_SP as sp
import copy

numberOfBacktracks = 0
def __init__(self,country) -> None:
    self.country_states = country.country_states
    self.country_neighbors = country.country_neighbors
    
def Forwardcheck(location, colors, color_options, heuristic = False):
    states = location[0]
    neighbor = location[1]
    global numberOfBacktracks
    all_none = True
    for value in colors.values():    #check if state is colored
        if(value is None):
            all_none = False
            break
    if all_none: return ("Success", numberOfBacktracks)
    if heuristic:
        currentState = cfs.minRemainingValueHeuristic(states, color_options, neighbor)
        new_color_options = cfs.leastConstrainingValueHeuristic(currentState, color_options, neighbor)
    else:
        currentState = states[0]
        new_color_options = color_options[currentState]
    currentNeighbors = neighbor[currentState]
    usedColors = list(map(colors.get, currentNeighbors))
    if None in usedColors:
        usedColors.remove(None)
    for color in new_color_options:
        if color not in usedColors:
            colors[currentState] = color
            states.remove(currentState) #remove current state from uncolored list
            if not cfs.check(color,currentNeighbors, colors, color_options):    #checking consistency
                previousColors = copy.deepcopy(color_options)
                color_options = cfs.reduce_color_options(color, currentNeighbors, colors, color_options)
                if fc.Forwardcheck((states,neighbor),colors,color_options)[0] != "Failure": #recursion
                    return ("Success", numberOfBacktracks)
                color_options = previousColors
            colors[currentState] = None
            states.append(currentState)
    if colors[currentState] == None:
        numberOfBacktracks += 1
        return ("Failure", numberOfBacktracks)