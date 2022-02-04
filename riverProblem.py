"""
Solution stub for the River Problem.

Fill in the implementation of the `River_problem` class to match the
representation that you specified in problem XYZ.
"""
from searchProblem import Search_problem, Arc

class River_problem(Search_problem):
    def start_node(self):
        """returns start node"""
        return ""
    
    def is_goal(self,node):
        """is True if node is a goal"""
        return node == "fghx"

    def neighbors(self,node):
        """returns a list of the arcs for the neighbors of node"""
        if node == "": 
            return [Arc("", "fh", 1)]
        elif node == "fh":
            return [Arc("fh", "h", 1), Arc("fh", "", 1)]
        elif node == "h":
            return [Arc("h", "fh", 1), Arc("h", "fgh", 1), Arc("h", "fxh", 1)]
        elif node == "g":
            return [Arc("g", "fgh", 1), Arc("g", "fgx", 1)]
        elif node == "x":
            return [Arc("x", "fgx", 1), Arc("x", "fxh", 1)]
        elif node == "fgh":
            return [Arc("fgh", "h", 1), Arc("fgh", "g", 1)]
        elif node == "fgx":
            return [Arc("fgx", "g", 1), Arc("fgx", "x", 1), Arc("fgx", "gx", 1)]
        elif node == "fxh":
            return [Arc("fxh", "h", 1), Arc("fxh", "x", 1)]
        elif node == "gx":
            return [Arc("gx", "fgx", 1), Arc("gx", "fghx", 1)]
        elif node == "fghx":
            return [Arc("fghx", "gx", 1)]

    def heuristic(self,n):
        """Gives the heuristic value of node n."""
        return 2*(3 - len(n)) - 1
    

