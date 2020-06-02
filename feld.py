class Feld:
    """
    Me is the docstring
    """
    data = None

    def __init__(self):
        self.data = [[0 for _ in range(9)] for _ in range(9)]

    def __str__(self):
        """
        Pretty-print the field
        """
        res = ""
        lineBorder = "+---+---+---+---+---+---+---+---+---+\n"
        for row in self.data:
            res += lineBorder
            for elem in row:
                res += "| " + str(elem) +  " "
            res += "|\n"
        res += lineBorder
        return res

    def getNextEmpty(self):
        for x in range(9):
            for y in range(9):
                if(self.getElem(x,y) == 0):
                    return (x,y)
        return (-1,-1)

    def getPossibleEntries(self, posX, posY):
        if(self.getElem(posX, posY) != 0):
            return set()
        res = set([x for x in range(1,10)])
        for x in range(9):
            # row
            tmp = self.getElem(x, posY)
            if(tmp in res):
                res.remove(tmp)
            # col
            tmp = self.getElem(posX, x)
            if(tmp in res):
                res.remove(tmp)
            # squar
            tmp = self.getElem(3*int(posX/3.0) + (x % 3), 3*int(posY/3.0) + int(x/3.0))
            if(tmp in res):
                res.remove(tmp)
        return res

    
    def getElem(self, x, y):
        return self.data[x][y]

    def setElem(self, x, y, val):
        """
        Check if this is a valid insertion
            if valid    -> true
            otherwise   -> false
        """

        if(val < 1 or val >9):
            return False

        # Check row
        rowSet = set([x for x in range(1,10)])
        for posX in range(9):
            tmp = self.getElem(posX, y)
            if(tmp in rowSet):
                rowSet.remove(tmp)
        if(not val in rowSet):
            return False

        # Check col
        colSet = set([x for x in range(1,10)])
        for posY in range(9):
            tmp = self.getElem(x,posY)
            if(tmp in colSet):
                colSet.remove(tmp)
        if(not val in colSet):
            return False

        # Check quadr
        quadrSet = set([x for x in range(1,10)])
        x0 = 3 * int(x/3.0)
        y0 = 3 * int(y/3.0)
        for xOffs in range(3):
            for yOffs in range(3):
                tmp = self.getElem(x0+xOffs, y0+yOffs)
                if(tmp in quadrSet):
                    quadrSet.remove(tmp)
        if(not val in quadrSet):
            return False



        self.data[x][y] = val
        return True


    def solved(self):
        """
        Check all entries, if they are valid and not empty
        """

        for x in range(9):
            for y in range(9):
                if(self.getElem(x,y) == 0):
                    return False

        return True