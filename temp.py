import json
import sys



class Hex:
    def __init__(self, x, y, color='n', parent = None):
        self.x = x
        self.y = y
        self.color = color
        # added attributes
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __str__(self):
        return f"({self.x},{self.y})"

    def dist(self, other):
        vec_x = (self.x - other.x)
        vec_y = (self.y - other.y)
        return (abs(vec_x) + abs(vec_y) + abs(vec_x + vec_y)) / 2

    def neighbor(self):
        neighbors = [Hex(self.x, self.y + 1), Hex(self.x + 1, self.y)]
        if self.x:
            neighbors.append(Hex(self.x - 1, self.y))
            neighbors.append(Hex(self.x - 1, self.y+1))
        if self.y:
            neighbors.append(Hex(self.x, self.y - 1))
            neighbors.append(Hex(self.x + 1, self.y - 1))
        return neighbors
    

# This is the entry point. class declaration below.
# Todo: After finishing class construction refactor code so Hex becomes a loadable module.


    
if __name__ == '__main__':
    testing = 0
    if testing:
        test = Hex(1, 1)
        test_a = Hex(0, 0)
        test_b = Hex(5, 5)
        print(test_a.dist(test_b))
        for i in test.neighbor():
            print(i)
    file = open(sys.argv[1])
    # data is a dict object
    data = json.load(file)

    # start working here
    start = Hex(data["start"][0], data["start"][1], None,)
    goal = Hex(data["goal"][0], data["goal"][1], None)
    board = []
    for i in data["board"]:
        board.append(Hex(i[1], i[2], i[0]))

    # debug 
    def astar():
        openlist = [] 
        closed = []
        openlist.append(start)
        current = start

        while len(openlist) > 0:
            cur_index = 0
            for index in range(len(openlist)):
                if openlist[index].f < openlist[cur_index].f:
                    cur_index = index
            
            current = openlist[cur_index]
            openlist.pop(cur_index)
            closed.append(current)


            if current == goal:
                print("Goal Found")
                path = []
                current_node = current
                while current_node is not None:
                    path.append(current_node)
                    current_node = current_node.parent
                return path

            for adjacent_hex in current.neighbor():
                next = Hex(adjacent_hex.x, adjacent_hex.y, current)
                neighbor = next
                if neighbor in board:
                    continue
                if neighbor not in closed:
                    temp = current.g + 1
                    if neighbor in openlist:
                        if neighbor.g > temp:
                            neighbor.g = temp
                    else:
                        neighbor.g = temp
                        openlist.append(neighbor)
                
                neighbor.h = neighbor.dist(goal)
                neighbor.f = neighbor.g + neighbor.h
    
                        



    path = astar()

    print(path)

    




# Done: need to get json parser up and running
# Done: implement distance calculation between two hex grid
# Update: test this Michael
# Todo: A star algorithm