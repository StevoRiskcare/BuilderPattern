# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Computers.accer import Accer
from Computers.mac_book_air import MacBookAir
from director import Director


def main():
    computer_builder = Director(MacBookAir())
    computer_builder.builder_board()
    computer = computer_builder.get_computer()
    computer.display()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
