from Computers.accer import Accer
from Computers.mac_book_air import MacBookAir
from director import Director


def main():
    computer_builder = Director(MacBookAir())
    computer_builder.builder_board()
    computer = computer_builder.get_computer()
    computer.display()



if __name__ == '__main__':
    main()


