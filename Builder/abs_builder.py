import abc

from Builder.abs_computer import Computer


class AbsBuilder(metaclass=abc.ABCMeta):
    def get_computer(self):
        return self._computer


    def new_computer(self):
        self._computer = Computer()

    @abc.abstractmethod
    def build_board(self):
        pass

