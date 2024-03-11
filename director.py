class Director(object):
    def __init__(self, builder):
        self._builder = builder

    def builder_board(self):
        self._builder.new_computer()
        self._builder.build_board()

    def get_computer(self):
        return self._builder.get_computer()