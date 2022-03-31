class Hex:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def dist(self, other):
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test = Hex(0, 0)
    print(test)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
