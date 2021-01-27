# import abc

class Game:
    class Status:
        pending = 0
        playing = 1
        stopped = 2
    
    def __init__(self):
        self.status = Game.Status.pending
        self.players = []

class Omok(Game):

    class Rule:
        free = 0
        standard = 1
        omok = 2
        renju = 3
        RIF = 4
        soosyrv = 5

    def __init__(self):
        super.__init__()
        self.move = 0
        self.moves = []
        self.board_size = 15
        self.board = [[0] * self.board_size] * self.board_size
        self.rule = Omok.Rule.renju

    def set_white(self, id):
        self.players.append(id)
        self.white = id

    def set_black(self, id):
        self.players.append(id)
        self.black = id

    def place(self, id, coord):
        if len(coord) != 2:
            raise Exception('InvalidCoordError')

        if not coord[0].isalpha() or not coord[1].isnumeric():
            raise Exception('InvalidCoordError')
        
        x = ord(coord[0].upper()) - ord('A')
        y = int(coord[1]) - 1

        if x >= self.board_size or y < 0 or y >= self.board_size:
            raise Exception('CoordError')
        
        if self.board[x][y] != 0:
            raise Exception('PlacementError')
        