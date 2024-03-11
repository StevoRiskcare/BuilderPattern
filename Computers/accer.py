from Builder.abs_builder import AbsBuilder


class Accer(AbsBuilder):
    def build_board(self):
        self._computer.intelCore = 13
        self._computer.ram = '16 GB'


