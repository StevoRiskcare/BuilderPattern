from Builder.abs_builder import AbsBuilder


class MacBookAir(AbsBuilder):
    def build_board(self):
        self._computer.cou = '8-core'
        self._computer.battery_life = '18 hours'
