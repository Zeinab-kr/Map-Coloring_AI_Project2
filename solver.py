import sys
import cv2
import random
from map import Map
import utils

ESCAPE_KEY_CHARACTER = 27
SLEEP_TIME_IN_MILLISECONDS = 500

GRAPH = {}
COLORED_STATES = {}
N_COLORS = 4
COLORING_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
NONE_COLOR = (0, 0, 0)
BACKTRACK_COUNT = 0

MAP = None
FILTERING_MODE = None
USE_VARIABLE_ORDERING = None
USE_VALUE_ORDERING = None


def colorize_map(manual = False):
    for i in range(len(MAP.nodes)):
        if (COLORED_STATES[i] == None):
            MAP.change_region_color(MAP.nodes[i], NONE_COLOR)
        else:
            MAP.change_region_color(MAP.nodes[i], COLORING_COLORS[COLORED_STATES[i]])
    cv2.imshow('Colorized Map', MAP.image)
    if not manual:
        key = cv2.waitKey(SLEEP_TIME_IN_MILLISECONDS)
    else:
        key = cv2.waitKey()
    if key == ESCAPE_KEY_CHARACTER:
        cv2.destroyAllWindows()
        exit()

'''BACKTRACKING CSP SOLVER'''
def backtrack_solve(domains):
    """
        returns True when the CSP is solved, and False when backtracking is neccessary
        
        you will need to use the global variables GRAPH and COLORED_STATES, refer to preprocess() and try to see what they represent
        use FILTERING_MODE, USE_VARIABLE_ORDERING, and USE_VALUE_ORDERING for branching into each mode
        FILTERING_MODE is either "-n", "-fc", or "ac", and the other two are booleans
        
        HINT: you may want to import deepcopy to generate the input to the recursive calls
        NOTE: remember to call colorize_map() after each value assingment for the graphical update
              use colorize_map(True) if you want to manually progress by pressing any key
        NOTE: don't forget to update BACKTRACK_COUNT on each backtrack
    """
    global BACKTRACK_COUNT
    if utils.is_solved(GRAPH, COLORED_STATES):
        print("solved")
        print(f"backtrack count: {BACKTRACK_COUNT}")
        colorize_map(True)
        exit(0)
      
    "*** YOUR CODE HERE ***"     
    

'''ITERATIVE IMPROVEMENT SOLVER'''
def iterative_improvement_solve(domains, max_steps=100):
    """
        you will need to use the global variables GRAPH and COLORED_STATES, refer to preprocess() and try to see what they represent
        don't forget to call colorize_map()
        1. initialize all the variables randomly,
        2. then change the conficting values until solved, use max_steps to avoid infinite loops
    """
    "*** YOUR CODE HERE ***"
    
    "*** YOUR CODE ENDS HERE ***" 
    print("solved")
    colorize_map(True)
            
            
def preprocess():
    MAP.initial_preprocessing()
    for vertex in range(len(MAP.nodes)):
       GRAPH[vertex], COLORED_STATES[vertex] = set(), None
    for v in MAP.nodes:
        for adj in v.adj:
            GRAPH[v.id].add(adj)
            GRAPH[adj].add(v.id)

def assign_boolean_value(argument):
    if argument == "-t":
        return True
    elif argument == "-f":
        return False
    else:
        return None


if __name__ == "__main__":
    try:
        MAP_IMAGE_PATH = sys.argv[1]
        FILTERING_MODE = sys.argv[2]
        is_ii_mode = FILTERING_MODE == "-ii"
        if not is_ii_mode:
            USE_VARIABLE_ORDERING = assign_boolean_value(sys.argv[3])
            USE_VALUE_ORDERING = assign_boolean_value(sys.argv[4])
            if USE_VARIABLE_ORDERING == None or USE_VALUE_ORDERING == None:
                print("invalid ordering flags")
                exit(1)
    except IndexError:
        print("Error: invalid arguments.")
        exit(1)
        
    try:
        MAP = Map(cv2.imread(MAP_IMAGE_PATH, cv2.IMREAD_COLOR))
    except Exception as e:
        print("Could not read the specified image")
        exit(1)
    
    preprocess()
    domains = [list(range(N_COLORS)) for _ in range(len(GRAPH.keys()))]
    if not is_ii_mode:
        print(f"filtering mode: {FILTERING_MODE}, use variable ordering: {USE_VARIABLE_ORDERING}, use value ordering: {USE_VALUE_ORDERING}")
        backtrack_solve(domains)
    else:
        iterative_improvement_solve(domains)
    