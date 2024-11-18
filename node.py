import math

class Node:
    # constructor with default params
    def __init__(self, name, distance=math.inf, parent=None):
        self.name = name
        self.distance = distance
        self.parent = parent

    def __lt__(self, other):
        # compares based on distance
        return self.distance < other.distance
    