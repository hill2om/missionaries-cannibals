class State:
    
    # instance initialization
    def __init__(self, m, c, boat, parent):
        self.m = m
        self.c = c
        self.boat = boat
        self.parent = parent
        self.children = []
    
    # print information about the current state
    def printState(self):
        print('m:', self.m, 'c:', self.c, self.boat)
    
    # function to check the state against the goal
    def isGoal(self):
        if self.m == 0 and self.c == 0 and self.boat == False:
            return True
        return False
    
    def createChildren(self):
        # if the boat is on the left side of the river
        # make sure that the # of missionaries and cannibals doesn't go below the minimum
        # ensure that there are never more cannibals on the bank
        if self.boat:
            c = 4
            for m in range(5):
                if (self.m - int(m/2)) >= 0 and (self.c - int(c/2)) >= 0:
                    if ((self.m - int(m/2)) == (self.c - int(c/2))) or (self.m - int(m/2)) == 0 or (self.m - int(m/2)) == 3:
                        self.children.append(State((self.m - int(m/2)), (self.c - int(c/2)), False, self))
                c -= 1
        # if the boat is on the right side of the river
        # make sure that the # of missionaries and cannibals don't go above the maximum
        # ensure that there are never more cannibals on the bank
        else:
            c = 4
            for m in range(5):
                if (self.m + int(m/2)) <= 3 and (self.c + int(c/2)) <= 3:
                    if ((self.m + int(m/2)) == (self.c + int(c/2))) or (self.m + int(m/2)) == 3 or (self.m + int(m/2)) == 0:
                        self.children.append(State((self.m + int(m/2)), (self.c + int(c/2)), True, self))
                c -= 1