import numpy as np
import constants
class Slice:

    def __init__(self,y1,x1,y2,x2):
        self.pizzaslice = constants.pizza[y1:y2+1,x1:x2+1]
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
        self.height = self.y2 - self.y1 + 1
        self.width = self.x2 - self.x1 + 1
        self.size = self.width * self.height
        self.mushrooms = 0
        for i in range(0,self.height):
            for j in range(0, self.width):
                if (self.pizzaslice[i][j] == 'M'):
                    self.mushrooms += 1
        self.tomatoes = self.size - self.mushrooms

    def getText(self):
        return str(self.y1) + " " + str(self.x1) + " " + str(self.y2) + " " + str(self.x2)

    def isValid(self, otherslices):
        if (self.size > constants.H):
            return False

        for slice in otherslices:
            if(self.overlaps(slice)):
                return False

        if self.mushrooms >= constants.L and self.tomatoes >= constants.L:
                return True

        return False

    def overlaps(self, otherslice):
        return self.x1 < otherslice.x1 + otherslice.width and (self.x1 + self.width) > otherslice.x1 \
               and self.y1 < otherslice.y1 +otherslice.height and self.y1 + self.height > otherslice.y1
