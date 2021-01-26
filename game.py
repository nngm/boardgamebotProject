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
        self.rule = Omok.Rule.renju

    def set_white(self, id):
        self.players.append(id)
        self.white = id

    def set_black(self, id):
        self.players.append(id)
        self.black = id

    def place(self, id, coord):
        