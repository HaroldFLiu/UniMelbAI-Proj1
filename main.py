class Hex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def dist(self, other):
        pass


# This is the entry point. class declaration below.
# Todo: After finishing class construction refactor code so Hex becomes a loadable module.
if __name__ == '__main__':
    test = Hex(0, 0)
    print(test)

# Todo: need to get json parser up and running
# Todo: implement distance calculation between two hex grid
# Todo: A star algorithm
