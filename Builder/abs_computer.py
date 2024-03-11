class Computer(object):
    def display(self):
        temp = vars(self)
        for item in temp:
            print('{}: {}'.format(temp[item], item))