class Hex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def dist(self, other):
        vec_x = (self.x - other.x)
        vec_y = (self.y - other.y)
        return (abs(vec_x) + abs(vec_y) + abs(vec_x + vec_y)) / 2


# This is the entry point. class declaration below.
# Todo: After finishing class construction refactor code so Hex becomes a loadable module.
if __name__ == '__main__':
    test = Hex(0, 0)
    test_a = Hex(0, 0)
    test_b = Hex(5, 5)
    print(test_a.dist(test_b))

# Todo: need to get json parser up and running
# Todo: implement distance calculation between two hex grid
# Update: test this Michael
# Todo: A star algorithm
