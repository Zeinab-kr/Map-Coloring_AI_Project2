import random

def is_consistent(graph, variable_value_pairs):
    """
        returns True if the variables that have been assigned a value so far are consistent with the constraints, 
        and False otherwise.
        
        variable_value_pairs can be used to access any value of any variable from the variable as a key
        you can use variable_value_pairs.items() to traverse it as (state, color) pairs
                    variable_value_pairs.keys() to get all the variables,         
                and variable_value_pairs.values() to get all the values
    """
    for state in variable_value_pairs.keys():
        if variable_value_pairs[state] is not None:
            for neighbor in graph[state]:
                if variable_value_pairs[neighbor] == variable_value_pairs[state]:
                    return False
    return True
    

def is_solved(graph, variable_value_pairs):
    """
        returns True if the CSP is solved, and False otherwise
    """
    for value in variable_value_pairs.values():
        if value is None:
            return False
    return is_consistent(graph, variable_value_pairs)
    

def get_next_variable(variable_value_pairs, domains):
    """
        returns the index of the next variable from the default order of the unassinged variables
    """
    for i in range(len(domains)):
        if variable_value_pairs[i] is None:
            return i
    return None
    

def get_chosen_variable(graph, variable_value_pairs, domains):
    """
        returns the next variable that is deemed the best choice by the proper heuristic
        use a second heuristic for breaking ties from the first heuristic
    """
    "*** YOUR CODE HERE ***"
    "MRV & degree heuristic"
    
    
def get_ordered_domain(graph, domains, variable):
    """
        returns the domain of the varibale after ordering its values by the proper heuristic
        (you may use imports here)
    """
    "*** YOUR CODE HERE ***"
    

def forward_check(graph, variable_value_pairs, domains, variable, value):
    """
        removes the value assigned to the current variable from its neighbors
        returns True if backtracking is necessary, and False otherwise
    """
    "*** YOUR CODE HERE ***"
    
def ac3(graph, variable_value_pairs, domains):
    """
        maintains arc-consistency
        returns True if backtracking is necessary, and False otherwise
    """
    "*** YOUR CODE HERE ***"
    


def random_choose_conflicted_var(graph, variable_value_pairs):
    """
        returns a random variable that is conflicting with a constrtaint
    """
    "*** YOUR CODE HERE ***"
    
def get_chosen_value(graph, variable_value_pairs, domains, variable):
    """
        returns the value by using the proper heuristic
        NOTE: handle tie-breaking by random
    """
    "*** YOUR CODE HERE ***"
    