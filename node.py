import constants
from slice import Slice
from heapq import heappush
class Node:
    node_slices = []
    score = 0
    estimate = 0
    mushrooms = 0
    tomatoes = 0
    def __init__(self, slices, score, estimate, newSlice, parentshrooms,parenttomatoes,root = False):
        if(root):
            self.score = 0
            self.estimate = constants.pizza.size
            for i in range(0, constants.R):
                for j in range(0, constants.C):
                    if(constants.pizza[i][j] == 'M'):
                        self.mushrooms+= 1

            self.tomatoes = constants.pizza.size - self.mushrooms
        else:
            self.node_slices = list(slices)
            self.node_slices.append(newSlice)
            self.mushrooms = parentshrooms - newSlice.mushrooms
            self.tomatoes = parenttomatoes - newSlice.tomatoes
            slice_size = newSlice.size
            self.score = score + slice_size
            self.estimate = estimate - slice_size

    def generate_children(self):
        if self.mushrooms == 0 or self.tomatoes == 0:
            return []
        L = constants.L
        pizza = constants.pizza
        C = constants.C
        R = constants.R
        H = constants.H
        nodes = []
        starty = 0
        startx=0
        for i in range(starty,R):
            for j in range(startx,C):
                for size in range(2*L, H+1):
                    for rows in range(1, size+1):
                        if len(nodes) > 100:
                            return nodes
                        if(size % rows == 0):
                            newcoord = (i+rows-1,j+(size/rows)-1)
                            if(newcoord[0] < R and newcoord[1]<C):
                                newSlice = Slice(int(i),int(j),int(newcoord[0]),int(newcoord[1]))
                                if(newSlice.isValid(self.node_slices)):
                                    newnode = Node(self.node_slices,self.score, self.estimate, newSlice, self.mushrooms, self.tomatoes)
                                    if(newnode.mushrooms >= constants.L and newnode.tomatoes >= constants.L):
                                        percentage = float(newnode.mushrooms) / (newnode.mushrooms + newnode.tomatoes)
                                        diff = abs(0.5 - percentage)
                                        heappush(nodes, (-newnode.score-(1-diff), newnode))

        return nodes
