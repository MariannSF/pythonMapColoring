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
    

def ForwardcheckSP(location, colors, color_options, heuristic=False):
    global numberOfBacktracks
    states = location[0]
    neighbor = location[1]
    all_none = all(value is None for value in colors.values())
    if all_none:
        return ("Success", numberOfBacktracks)

    if heuristic:
        currentState = cfs.minRemainingValueHeuristic(states, color_options, neighbor)
        new_color_options = cfs.leastConstrainingValueHeuristic(currentState, color_options, neighbor)
    else:
        currentState = states[0]
        new_color_options = color_options[currentState]

    currentNeighbors = neighbor[currentState]
    usedColors = [colors[neighbor] for neighbor in currentNeighbors if colors[neighbor] is not None]

    for color in new_color_options:
        if color not in usedColors:
            colors[currentState] = color
            states.remove(currentState)

            if not cfs.check(color, currentNeighbors, colors, color_options):
                previousColors = copy.deepcopy(color_options)
                color_options = cfs.reduce_color_options(color, currentNeighbors, colors, color_options)

                if cfs.singleton_check(currentNeighbors, neighbor, colors, color_options):
                    if ForwardcheckSP((states, neighbor), colors, color_options)[0] != "Failure":
                        return ("Success", numberOfBacktracks)

                color_options = previousColors

            colors[currentState] = None
            states.append(currentState)

    if colors[currentState] is None:
        numberOfBacktracks += 1
        return ("Failure", numberOfBacktracks)
