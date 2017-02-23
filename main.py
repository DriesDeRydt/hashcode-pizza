import numpy as np
from slice import Slice
from node import Node
import constants
from heapq import heappop
import heapq
import to_file

def score(slices):
    return sum([slice.size for slice in slices])

with open('medium.in') as f:
    metadata = f.readline().replace('\n', '').split(' ')
    constants.R = int(metadata[0])
    constants.C = int(metadata[1])
    constants.L = int(metadata[2])
    constants.H = int(metadata[3])
    pizza = np.chararray((constants.R, constants.C))

    for i in range(0,constants.R):
        trimmedLine = f.readline().replace('\n', '')
        pizza[i] = list(trimmedLine)
    constants.pizza = pizza
#
#
# slice2 = Slice(0,3,5,5, pizza)
# print slice1.overlaps(slice2)
# print slice1.isValid([slice2], L, H)
# print score([slice1, slice2])
node = Node([],0,0,None, 0,0,root=True)
done = False
bestScore = 0
bestslices = None
open_set = [(0,node)]
index = 0
while not done:
    bestChild = heappop(open_set)
    bestNewNode = bestChild[1]
    if(bestNewNode.score > bestScore):
        bestScore = bestNewNode.score
        bestslices = list(bestNewNode.node_slices)
        to_file.to_file(bestslices)
        print "new best score: " + str(bestScore)
    open_set = list(heapq.merge(open_set, bestNewNode.generate_children()))

    if(index % 200 == 0 and (bestslices) is not None):
        to_file.to_file(bestslices)

    if(len(open_set) == 0):
        break
    if bestNewNode.score == constants.C * constants.R:
        bestslices = list(bestNewNode.node_slices)
        break
    index+=1


to_file.to_file(bestslices)
test = True
