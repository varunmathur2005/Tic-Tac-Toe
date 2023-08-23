# Tic-Tac-Toe Game
import sys

import fontstyle

import random


def main():
    choice = game_initialization()
    if choice == 1:
        print(fontstyle.apply("1. 2-Player Mode ", "bold/Italic/blue") + "\n")
        print(fontstyle.apply("2. Player V/S Computer (!UNDER DEVELOPMENT!) ", "bold/Italic/blue"))
        n = int(input(fontstyle.apply("Enter Your Choice: ", "bold/Italic/UNDERLINE/red")))
        if n == 1:
            player_2()
            rep = replay()
            if rep == True:
                main()
        if n == 2:
            sys.exit("UNDER DEVELOPMENT!")

    if choice == 2:
        how_to_play()


def game_initialization():
    print("\n")
    print("================================")
    print(fontstyle.apply("Welcome To Tic-Tac-Toe!", "bold/Italic/UNDERLINE/red"))
    print("================================\n")
    print(fontstyle.apply("1. Start New Game", "bold/Italic/blue") + "\n")
    print(fontstyle.apply("2. How To Play", "bold/Italic/blue") + "\n")
    print(fontstyle.apply("3. Quit", "bold/Italic/blue") + "\n")
    print("================================")
    print("--------------------------------")
    print("================================")

    while True:
        try:
            choice = int(
                input(
                    fontstyle.apply("Enter Your Choice: ", "bold/Italic/UNDERLINE/red")
                )
            )
            if choice not in [1, 2, 3, 4]:
                sys.exit("Invalid Choice")
            if choice == 3:
                print("\n")
                sys.exit(
                    fontstyle.apply("Thanks For Playing!", "bold/Italic/UNDERLINE/red")
                )

        except ValueError:
            sys.exit(fontstyle.apply("INVALID CHOICE", "bold/Italic/UNDERLINE/red"))
        else:
            return choice


################################################################### 2 Player code ###################################################################
def player_2():
    player1, player2 = character()
    global board
    board = ["test", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    result = 0

    if player1 == "X":
        print_board(board)
        while not board_full(board):
            if check_win(player2, board) == True:
                result = 2
                break
            if check_win(player2, board) == False:
                player_move(player1, board)
                if check_win(player1, board) == True:
                    result = 1
                    break
                player_move(player2, board)
                print_board(board)
            else:
                if result != 1 or result != 2:
                    result = 0
                break

    if player1 == "O":
        print_board(board)
        while not board_full(board):
            if check_win(player2, board) == True:
                result = 2
                break
            if check_win(player1, board) == False:
                player_move(player2, board)
                if check_win(player2, board) == True:
                    result = 2
                    break
                player_move(player1, board)
                print_board(board)
            else:
                if result != 1 or result != 2:
                    result = 0
                break

    if result == 0:
        print(fontstyle.apply("GAME TIED", "bold/Italic/UNDERLINE/red"))
    if result == 1:
        print(fontstyle.apply("PLAYER 1 WINS!", "bold/Italic/UNDERLINE/red"))
    if result == 2:
        print(fontstyle.apply("PLAYER 2 WINS!", "bold/Italic/UNDERLINE/red"))


def check_win(char, board):
    if (
        (board[1] == board[2] == board[3] == char)
        or (board[4] == board[5] == board[6] == char)
        or (board[7] == board[8] == board[9] == char)
        or (board[1] == board[4] == board[7] == char)
        or (board[2] == board[5] == board[8] == char)
        or (board[3] == board[6] == board[9] == char)
        or (board[1] == board[5] == board[9] == char)
        or (board[3] == board[5] == board[7] == char)
    ):
        return True
    else:
        return False


def player_move(char, board):
    if board_full(board):
        return
    while True:
        try:
            n = int(
                input(fontstyle.apply("ENTER POSITION (1-9): ", "bold/Italic/blue"))
            )
            if 0 < n < 10:
                if check_space(n, board) == True:
                    place_char(char, n, board)
                    print_board(board)
                    break
                else:
                    print(fontstyle.apply("PLACE IS OCCUPIED!", "bold/Italic/red"))
            else:
                print(fontstyle.apply("INVALID INPUT!", "bold/Italic/red"))
        except ValueError:
            print(fontstyle.apply("INVALID INPUT!", "bold/Italic/red"))
            continue


def board_full(board):
    for _ in range(1, 10):
        if board[_] == " ":
            return False
    else:
        return True


def check_space(space, board):
    if board[space] == " ":
        return True


def place_char(char, place, board):
    board[place] = char


def character():
    characters = ["X", "O"]
    player1 = random.choice(characters)
    if player1 == "X":
        print(fontstyle.apply("Player 1 is X!: ", "bold/Italic/blue"))
        print(fontstyle.apply("Player 2 is O!: ", "bold/Italic/blue"))
        return ("X", "O")
    elif player1 == "O":
        print(fontstyle.apply("Player 1 is 0!: ", "bold/Italic/blue"))
        print(fontstyle.apply("Player 2 is X!: ", "bold/Italic/blue"))
        return ("O", "X")


def print_board(board):
    global a
    print("\n")
    a = "  {1}  |  {2}  |  {3}  \n-----------------\n  {4}  |  {5}  |  {6}  \n-----------------\n  {7}  |  {8}  |  {9}  \n"
    print()
    print(a.format(*board))


def replay():
    while True:
        try:
            n = input(
                fontstyle.apply(
                    "Enter 'Y' , 'y' to play again or Enter 'N' , 'n' to exit: ",
                    "bold/Italic/blue",
                )
            )
            if n in ["N", "n"]:
                sys.exit(
                    fontstyle.apply("THANKS FOR PLAYING!", "bold/Italic/UNDERLINE/red")
                )
            elif n in ["Y", "y"]:
                return True
            else:
                print(fontstyle.apply("Invalid Input!", "bold/Italic/red"))
        except ValueError:
            print(fontstyle.apply("Invalid Input!", "bold/Italic/red"))


################################################################### 2 Player code ###################################################################


def how_to_play():
    with open("rules.txt", "r") as f:
        contents = f.read()
        print(contents)


if __name__ == "__main__":
    main()
