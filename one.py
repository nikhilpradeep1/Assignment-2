from cmd import IDENTCHARS
from contextlib import nullcontext
from platform import node


class dataStructure:
    node = None
    ID = None
    nodeDict = {node:ID}
    nodeID = {ID:node}

    def __init__(self, node, ID):
        nodeDict = {node:ID}
        nodeID = {ID:node}

    def getID(self, node):
        return nodeDict[node]


