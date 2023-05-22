class CircleCrossGame:
    def __init__(self):
        self.field = [0 for i in range(9)]

    def set_cross(self, index):
        self.field[index] = 1

    def set_circle(self, index):
        self.field[index] = 2

    def printField(self):
        for i in range(3):
            for j in range(3):
                if self.field[i * 3 + j] == 1:
                    symbol = "X"
                elif self.field[i * 3 + j] == 2:
                    symbol = "O"
                else:
                    symbol = i * 3 + j + 1
                print(symbol, end="")
                if j < 2:
                    print("\t|\t", end="")
            print()
            if 0 <= i < 2:
                print("_\t|\t_\t|\t_")

    def check_result(self):
        # 0 - continue game
        # 1 - cross wins
        # 2 - circle wins
        # 3 - draw
        for i in range(3):  # horizontal lines check
            if self.field[i] != 0 and self.field[i] == self.field[i + 1] and self.field[i] == self.field[i + 2]:
                return self.field[i]
        for i in range(3):  # vertical lines check
            if self.field[i] != 0 and self.field[i] == self.field[i + 3 and self.field[i]] == self.field[i + 6]:
                return self.field[i]
        # X lines check
        if self.field[4] != 0:
            if (self.field[0] == self.field[4] and self.field[0] == self.field[8]) or (
                    self.field[2] == self.field[4] and self.field[2] == self.field[6]):
                return self.field[4]
        # empty spaces check
        for i in range(len(self.field)):
            if self.field[i] == 0:
                return 0
        return 3
