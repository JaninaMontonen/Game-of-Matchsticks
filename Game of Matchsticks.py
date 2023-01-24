"""
COMP.CS.100 Programming 1
Student ID: 050015443
Name: Janina Montonen
E-mail: janina.montonen@tuni.fi
Project 1: Game of Matchsticks

With this program two users can play the Game of Matchsticks.
"""

STICKS = 21


def main():
    print("Game of sticks")
    sticks_left = STICKS

    while sticks_left > 0:
        to_pick = 4
        while to_pick != 1 and to_pick != 2 and to_pick != 3:
            to_pick = int(input("Player 1 enter how many sticks to remove: "))
            if to_pick != 1 and to_pick != 2 and to_pick != 3:
                print("Must remove between 1-3 sticks!")

        if sticks_left - to_pick <= 0:
            print("Player 1 lost the game!")
            sticks_left -= to_pick
            break
        else:
            print("There are", sticks_left - to_pick, "sticks left")
            sticks_left -= to_pick

        to_pick = 4
        while to_pick != 1 and to_pick != 2 and to_pick != 3:
            to_pick = int(input("Player 2 enter how many sticks to remove: "))
            if to_pick != 1 and to_pick != 2 and to_pick != 3:
                print("Must remove between 1-3 sticks!")

        if sticks_left - to_pick <= 0:
            print("Player 2 lost the game!")
            sticks_left -= to_pick
        else:
            print("There are", sticks_left - to_pick, "sticks left")
            sticks_left -= to_pick


if __name__ == "__main__":
    main()