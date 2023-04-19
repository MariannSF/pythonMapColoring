import copy
from datetime import datetime
import CFS as cfs
import DFS as dfs
import DFS_FC as fc
import DFS_FC_SP as sp

color_options = {}


def color_dict(states):
    assignedColor = {}
    for state in states:
        assignedColor[state] = None
    return assignedColor


def create_color_options(states, numberOfColors):
    color_options = {}
    color_choices = ['Red', 'Blue', 'Green', 'Yellow', 'Pink', 'Orange', 'Black', 'Grey', 'Purple', 'White']
    color = []
    for i in range(numberOfColors):
        color.append(color_choices[i])
    for state in states:
        color_options[state] = copy.deepcopy(color)
    return color_options


def reduce_color_options(color, currentNeighbors, colors, color_options):
    for neighbor in currentNeighbors:
        if colors[neighbor] == None and color in color_options[neighbor]:
            color_options[neighbor].remove(color)
    return color_options


def check(color, currentNeighbors, colors, color_options):
    for neighbor in currentNeighbors:
        if colors[neighbor] == None and color in color_options[neighbor]:
            if len(color_options[neighbor]) == 1:
                return True
    return False


def singleton_check(currentNeighbors, neighbors, colors, color_options):
    reduceStates = []
    for neighbor in currentNeighbors:
        if len(color_options[neighbor]) == 1 and colors[neighbor] == None:
            reduceStates.append(neighbor)

    while reduceStates:
        state = reduceStates.pop(0)
        for neighbor in neighbors[state]:
            if colors[neighbor] == None and color_options[state][0] in color_options[neighbor]:
                color_options[neighbor].remove(color_options[state][0])
                if len(color_options[neighbor]) == 0:
                    return False
                if len(color_options[neighbor]) == 1:
                    reduceStates.append(neighbor)
    return True


def minRemainingValueHeuristic(states, color_options, neighbors):
    states.sort(key=lambda x: (len(color_options[x]), -len(neighbors[x])))
    currentSelection = states[0]
    return currentSelection


def leastConstrainingValueHeuristic(currentState, color_options, neighbors):
    currentcolor_options = color_options[currentState]
    currentNeighbors = neighbors[currentState]
    orderedcolor_options = {}
    for color in currentcolor_options:
        count = 0
        for neighbor in currentNeighbors:
            if color in color_options[neighbor]:
                count = count + 1
        orderedcolor_options[color] = count

    orderedcolor_options = dict(sorted(orderedcolor_options.items(), key=lambda item: item[1]))
    return list(orderedcolor_options.keys())


def getChromaticNumber(location):
    states = location[0]
    neighbor = location[1]
    count = 0
    while True:
        count += 1
        copyStates = copy.deepcopy(states)
        colors = color_dict(states)
        color_options = create_color_options(states, count)
        result = dfs.DFS_Only((copyStates, neighbor), colors, color_options)
        if result[0] != "Failure":
            break
    return count


def checkConstraint(state, neighbors, color, colors):
    for neighbor in neighbors[state]:
        if colors[neighbor] == color:
            return False
    return True