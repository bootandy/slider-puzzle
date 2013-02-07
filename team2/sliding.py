import pprint

class Board:

    def __init__(self, n):
        self.n = n
        self.board = dict(((i,j),j*n+i) for i in range(n) for j in range(n))
        self.gap_num = self.n**2 - 1

    def __repr__(self):
        res = ""
        for j in range(self.n):
            for i in range(self.n):
                number = self.board[(i,j)]
                if number != self.gap_num:
                    res += "%s" % (number + 1)
                else:
                    res += ' '
            res += "\n"
        return res


    def find_gap(self):
        gap = None
        for j in  range(self.n):
            for i in range(self.n):
                    if self.board[(i,j)] == self.gap_num:
                        gap = (i,j)
                        break
            if gap is not None:
                break
        assert gap != None
        return gap


    def possible_moves(self):
        res = []
        gap = self.find_gap()
        (i,j) = gap
        if i >= 1:
            res.append((i-1, j))
        if i < self.n-1:
            res.append((i+1, j))
        if j >= 1:
            res.append((i, j-1))
        if j < self.n-1:
            res.append((i, j+1))
        assert len(res) > 0

        return res

    def check_if_finished(self):
        number_list = []
        for j in range(self.n):
            for i in range(self.n):
                number = self.board[(i, j)]
                if number != j*self.n + i and (number != self.gap_num and i == self.n -1 and j == self.n -1):
                    return False
        return True

    def slide(self, tile):
        gap = b.find_gap()
        self.board[tile], self.board[gap] = self.board[gap], self.board[tile]


if __name__ == "__main__":
    b = Board(3)
    print b
    print b.check_if_finished()
    print b.possible_moves()

    while not b.check_if_finished():
        moves = b.possible_moves()
        b.slide(moves[0])
        print b
