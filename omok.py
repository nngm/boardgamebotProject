class Status:
    pending = 1
    playing = 2
    stopped = 3
    
class Omok:

    class Rule:
        free = 1
        standard = 2
        omok = 3
        renju = 4
        RIF = 5
        soosyrv = 6

    def __init__(self, id1, id2):
        self.status = Status.pending
        self.move = 0
        self.player1 = id1
        self.player2 = id2
        self.board_size = 15
        self.rule = Omok.Rule.renju
        self.black = self.player1
        self.white = self.player2