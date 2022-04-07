import json
import sys


class Hex:
    def __init__(self, r, q, color='n', parent=None):
        self.r = r
        self.q = q
        self.color = color
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __str__(self):
        return f"({self.r},{self.q})"

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.r == other.r and self.q == other.q
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        if isinstance(self.__class__, other):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def dist(self, other):
        vec_r = (self.r - other.r)
        vec_q = (self.q - other.q)
        return (abs(vec_r) + abs(vec_q) + abs(vec_r + vec_q)) / 2

    def neighbor(self):
        neighbors = [Hex(self.r, self.q + 1, parent=self), Hex(self.r + 1, self.q, parent=self)]
        if self.r:
            neighbors.append(Hex(self.r - 1, self.q, parent=self))
            neighbors.append(Hex(self.r - 1, self.q + 1, parent=self))
        if self.q:
            neighbors.append(Hex(self.r, self.q - 1, parent=self))
            neighbors.append(Hex(self.r + 1, self.q - 1, parent=self))
        return neighbors


# This is the entry point. class declaration below.



if __name__ == '__main__':

    file = open(sys.argv[1])
    # data is a dict object
    data = json.load(file)

    # start working here
    boardsize = data["n"]
    start = Hex(data["start"][0], data["start"][1], 'n')
    goal = Hex(data["goal"][0], data["goal"][1], 'n')
    board = []
    for i in data["board"]:
        board.append(Hex(i[1], i[2], i[0]))

    # start a star
    target = [start]
    while len(target):
        pass


    def astar():
        opened = []
        closed = []
        opened.append(start)
        current = start

        while len(opened) > 0:
            cur_index = 0
            for index in range(len(opened)):
                if opened[index].f < opened[cur_index].f:
                    cur_index = index

            # explore this
            current = opened[cur_index]
            #print(current)
            opened.pop(cur_index)
            closed.append(current)

            if current == goal:
                path = []
                current_node = current
                while current_node is not None:
                    path.append(current_node)
                    current_node = current_node.parent
                return path

            for adjacent_hex in current.neighbor():
                neighbor = adjacent_hex
                # check if hex is on the board
                if neighbor.r not in range(0, boardsize):
                    continue
                if neighbor.q not in range(0, boardsize):
                    continue

                # if used don't bother
                if neighbor in board:
                    continue
                if neighbor not in closed:
                    next = current.g + 1
                    if neighbor in opened:
                        if neighbor.g > next:
                            neighbor.g = next
                    else:
                        neighbor.g = next
                        opened.append(neighbor)

                neighbor.h = neighbor.dist(goal)
                neighbor.f = neighbor.g + neighbor.h


    path = astar()
    if path == None:
        print(0)
    else:
        print(len(path))
        for i in path[::-1]:
            print(i)
    

