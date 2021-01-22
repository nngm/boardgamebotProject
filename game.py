import abc

class Game(metaclass=abc.ABCMeta):
    class Status:
        pending = 1
        playing = 2
        stopped = 3

    @abc.abstractmethod
    def __init__(self, players):
        self.status = Game.Status.pending
        self.players = players