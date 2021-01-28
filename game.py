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

    black = 1
    white = 2

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
        self.color = {}

    def set_black(self, id):
        self.players.append(id)
        self.black = id
        self.color[id] = Omok.black

    def set_white(self, id):
        self.players.append(id)
        self.white = id
        self.color[id] = Omok.white
    
    def is33(self, x, y, color):
        # 
        return False

    def is44(self, x, y, color):
        # 
        return False

    def isoverline(self, x, y, color):
        # 
        return False

    def isforbidden(self, x, y, color):
        if self.rule == Omok.Rule.free or self.rule == Omok.Rule.standard:
            return False
        
        if self.rule == Omok.Rule.omok:
            return self.is33(x, y, color)
        
        if self.rule == Omok.Rule.renju:
            if color == Omok.white:
                return False
            else:
                return (self.is33(x, y, color) or self.is44(x, y, color)
                        or self.isoverline(x, y, color))

    def place(self, id, coord):
        if len(coord) != 2:
            raise TypeError

        if not coord[0].isalpha() or not coord[1].isnumeric():
            raise TypeError
        
        x = ord(coord[0].upper()) - ord('A')
        y = int(coord[1]) - 1

        if x >= self.board_size or y < 0 or y >= self.board_size:
            raise Exception('CoordError')
        
        if self.board[x][y] != 0:
            raise Exception('PlacementError')
        
        if self.isforbidden(x, y, self.color[id]):
            raise Exception('ForbiddenMoveError')
        
        self.board[x][y] = self.color[id]
        