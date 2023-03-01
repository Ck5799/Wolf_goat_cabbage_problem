from search import *

class WolfGoatCabbage(Problem):
     def __init__(self, initial=('G', 'F', 'C', 'W'), goal=set()):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)

 
     def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = [{"F"}, {"F","G"}, {"F","W"},{"F","C"}]
        impossible_states =[{"W","G"},{"G","C"},{"F","W"},{"C",'G',"W"},{"F","C"},{"F"}]
        valid_actions =[]

        for action in possible_actions:
            result1=self.result(state,action)
            if result1 in impossible_states:
                continue
            else:
                valid_actions.append(action)
            # print(tuple(result1) == impossible_states, tuple(result1), impossible_states)
            # if sorted(tuple(result1)) in impossible_states:
            #     possible_actions.remove(action)
            #     continue
            # if ('F' not in result1) and('W'in result1)and('G'in result1)and ('W' not in result1):
            #     continue
            # elif ('F' not in result1) and('C'in result1)and('G'in result1)and ('W' in result1):
            #     continue
            # elif ('F' in result1)and('C'in result1)and('G'not in result1)and ('W' not in result1):
            #     continue
            # elif ('F' in result1)and('W'in result1)and('G'not in result1)and ('C'not in result1):
            #     continue
            # else:
            #     possible_actions.append(action)

            
            
        return valid_actions

        
        # if sorted(state) ==  sorted(("F","G","C","W")):
        #     possible_actions.remove(("F","C"))
        #     possible_actions.remove(("F","W"))
        #     possible_actions.remove(("F"))
            # return possible_actions
        
        # elif sorted(state) in sorted(("W","C")):
        #     possible_actions.remove(("F","G"),("F","W"),("F","C"))
        #     # return possible_actions
        
        # elif sorted(state) in sorted(("F","W","C")):
        #     possible_actions.remove(("F"),("F","G"))
        #     # return possible_actions
            
        # elif sorted(state) in sorted(("C",)):
        #     possible_actions.remove(("F"),("F","C"),("F","W"))
        #     # return possible_actions
        
        # elif sorted(state) in sorted(("F","C","G")):
        #     possible_actions.remove( ("F","G"), ("F","W"),("F"))
        #     # return possible_actions
        
        # elif sorted(state) in sorted(("W",)):
        #     possible_actions.remove(("F","C"),("F"),("F","C"),("F","W"))
        #     # return possible_actions
        
        # elif sorted(state) in sorted(("G",)):
        #     possible_actions.remove(("F","G"), ("F","W"),("F","C"))
        #     # return possible_actions          
        
        # print(possible_actions)
        #return possible_actions

        # if state==("F","G","C","W"):
        #     possible_actions.remove("W","C")
        #     return possible_actions
        
        # if state==("W","C"):
        #     possible_actions.remove("G")
        #     return possible_actions
        
        # if state==("F","W","C"):
        #     possible_actions.remove("G")
        #     return possible_actions
            
        # if state==("C"):
        #     possible_actions.remove("W","C")
        #     return possible_actions
        
        # if state==("F","C","G"):
        #     possible_actions.remove("W","G")
        #     return possible_actions
        
        # if state==("W"):
        #     possible_actions.remove("C")
        #     return possible_actions
        
        # if state==("G"):
        #     possible_actions.remove("W","C")
        #     return possible_actions          
        
     def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """
       
        result=set(state) 
        
        if  "F" in result:
            result = result.difference(action)
    
        else :
            result=result.union(action)

        
        
        return frozenset(result)
     
     def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        return state == self.goal
     

if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    #print(wgc.result(("F","C","W","G"),("F","G")))
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution) 