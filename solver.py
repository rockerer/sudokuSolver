import copy
from feld import *

class Solver():
    """
    Braindead backtracing algo for
    finding a sudoku solution
    """
    f = None
    tries = 0
    def __init__(self, f):
        self.f = f

    def solve(self):
        return(self.mySolve( self.f))

    def mySolve(self, f : Feld):
        self.tries += 1
        """
        find next empty element, copy f and insert all values
        """
        nextPos = f.getNextEmpty()
        if(nextPos == (-1, -1)):
            return f
        possibleEntries = f.getPossibleEntries(nextPos[0], nextPos[1])
        for elem in possibleEntries:
            newF = copy.deepcopy(f)
            newF.setElem(nextPos[0], nextPos[1], elem)
            res = self.mySolve(newF)
            if(res):
                return res



        # if not returned a valid feld no solution was found
        return False
