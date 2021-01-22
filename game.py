# import abc

class Game:
    class Status:
        pending = 0
        playing = 1
        stopped = 2

    def __init__(self, players):
        self.status = Game.Status.pending
        self.players = players

class Omok(Game):

    class Rule:
        free = 0
        standard = 1
        omok = 2
        renju = 3
        RIF = 4
        soosyrv = 5

    def __init__(self, id1, id2):
        super.__init__([id1, id2])
        self.move = 0
        self.moves = []
        self.board_size = 15
        self.rule = Omok.Rule.renju
        self.black = self.players[0]
        self.white = self.players[1]