# Tic-Tac-Toe Game
import sys

import fontstyle

import random

import random
import time
from datetime import date, datetime
import mysql.connector
 
# initialising mySQL connection
mydb = mysql.connector.connect(host="localhost", user="root", password="varunmathur")
mycursor = mydb.cursor()

# mySQL code + file handling
class ImpVar:
    """stores important variables for use anywhere"""
 
    win_counter, loss_counter = 0, 0
    tied_counter, match_counter = 0, 0
    move_counter = 0
    today = date.today()
    now = datetime.now()
    date = today.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")
    res_stmnt = None

def clean_slate(today, now):
     """resets all impvar values"""
     ImpVar.win_counter, ImpVar.loss_counter = 0, 0
     ImpVar.tied_counter, ImpVar.match_counter = 0, 0
     ImpVar.date = today.strftime("%Y-%m-%d")
     ImpVar.time = now.strftime("%H:%M:%S")
 
 
def file_init():
    """first initialisation of record file"""
    f1 = open("RECORD.TXT", 'w')  # writes recent session's summary to file
    f1.write("~" * 30 + "\n")
    f1.close()
 
 
def data_check(dt_name, d_type):
    """used for checking if database or table exists"""
    sql_check = False
    for x in mycursor:
        if x[0] == dt_name:
            sql_check = True
    if sql_check == False and d_type == "D":
        mycursor.execute("create database data")
    if sql_check == False and d_type == "T":
        mycursor.execute("create table scores(sDate {1}, sTime {1}, sMatches {0}, sWins {0}, sLosses {0}, sTied {0})".format("int(3)", "varchar(20)"))

 
 
def display():
    """display mysql content"""
    db = mysql.connector.connect(host="localhost", user="root", password="varunmathur", database="data")
    cursor = db.cursor()
    cursor.execute("select * from scores")
    results = cursor.fetchall()
    if len(results) == 0:
        print("Empty set!")
        return
    print()
    print("+----------+----------+----------------+------+--------+------+------+\n"
          "| Date     | Time     | Matches Played | Wins | Losses | Tied | Win% |\n"
          "+----------+----------+----------------+------+--------+------+------+")
    for i in results:
        win_percent = int(i[3]/i[2] * 100)
        i += (win_percent,)
        print("| {} | {} | {:<14} | {:<4} | {:<6} | {:<4} | {:<4} |".format(*i))
    print("+----------+----------+----------------+------+--------+------+------+")
 
 


def main():
    choice = game_initialization()
    if choice == 1:
        print(fontstyle.apply("1. 2-Player Mode ", "bold/Italic/blue") + "\n")
        print(fontstyle.apply("2. Player V/S Computer (!UNDER DEVELOPMENT!) ", "bold/Italic/blue"))
        n = int(input(fontstyle.apply("Enter Your Choice: ", "bold/Italic/UNDERLINE/red")))
        if n == 1:
            file_init()
            while True:
                print("-" * 28)
                player_2()
                print()
                time.sleep(1.5)
 
                f1 = open("RECORD.TXT", 'a')  # writes recent session's summary to file
                f1.write("{0} | Match Number: {1}\n".format(ImpVar.date, str(ImpVar.match_counter)))
                f1.write("Result: {}\n".format(ImpVar.res_stmnt))
                f1.write("~" * 30 + "\n")
            
                rep = replay()
                if rep == 1:
                    continue
                if rep == 0:
                   mycursor.execute("insert into scores values(\"{0}\", \"{1}\", {2}, {3}, {4}, {5})".format(ImpVar.date, ImpVar.time, ImpVar.match_counter, ImpVar.win_counter, ImpVar.loss_counter, ImpVar.tied_counter))
                   mydb.commit()
    
                    # inserting data into files
                   f1 = open("RECORD.TXT", "a")
                   f1.write("Total number of matches played: {}".format(str(ImpVar.match_counter)))
                   break
           
        if n == 2:
            sys.exit("UNDER DEVELOPMENT!")

    elif choice == 2:
        how_to_play()

    elif choice == 3:
        f1 = open("RECORD.TXT", 'r')
        r = f1.read()
        print("\n" + r)
        print(input("Press Enter to continue"), end="") 

    elif choice == 4:
        display()
        print(input("Press Enter to continue"), end="")
    
    elif choice == 5:
                print("\n")
                sys.exit(
                    fontstyle.apply("Thanks For Playing!", "bold/Italic/UNDERLINE/red")
                )  
    
     
        


def game_initialization():
    mycursor.execute("show databases")
    data_check("data", "D")  # checks if database is present
    mycursor.execute("use data")
    mycursor.execute("show tables")  # checks if table is present
    data_check("scores", "T")
    clean_slate(ImpVar.today, ImpVar.now)
    print("\n")
    print("================================")
    print(fontstyle.apply("Welcome To Tic-Tac-Toe!", "bold/Italic/UNDERLINE/red"))
    print("================================\n")
    print(fontstyle.apply("1. Start New Game", "bold/Italic/blue") + "\n")
    print(fontstyle.apply("2. How To Play", "bold/Italic/blue") + "\n")
    print(fontstyle.apply("3. Show Previous Session Summary", "bold/Italic/blue") + "\n")
    print(fontstyle.apply("4. Show All Time Scores", "bold/Italic/blue") + "\n")
    print(fontstyle.apply("5. Quit", "bold/Italic/blue") + "\n")
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
            if choice not in [1, 2, 3, 4, 5]:
                sys.exit("Invalid Choice")

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
        ImpVar.tied_counter += 1
        ImpVar.res_stmnt = "GAME TIED"
        print(fontstyle.apply(ImpVar.res_stmnt, "bold/Italic/UNDERLINE/red"))
    if result == 1:
        ImpVar.win_counter += 1
        ImpVar.res_stmnt = "PLAYER 1 WINS!"
        print(fontstyle.apply(ImpVar.res_stmnt, "bold/Italic/UNDERLINE/red"))
    if result == 2:
        ImpVar.loss_counter += 1
        ImpVar.res_stmnt = "PLAYER 2 WINS!"
        print(fontstyle.apply(ImpVar.res_stmnt, "bold/Italic/UNDERLINE/red"))
    
    ImpVar.match_counter += 1  # counts matches played


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
        print(fontstyle.apply("Player 1 is X! ", "bold/Italic/blue"))
        print(fontstyle.apply("Player 2 is O! ", "bold/Italic/blue"))
        return ("X", "O")
    elif player1 == "O":
        print(fontstyle.apply("Player 1 is 0! ", "bold/Italic/blue"))
        print(fontstyle.apply("Player 2 is X! ", "bold/Italic/blue"))
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
                rep = 0
                break
            elif n in ["Y", "y"]:
                rep = 1
                break
            else:
                print(fontstyle.apply("Invalid Input!", "bold/Italic/red"))
        except ValueError:
            print(fontstyle.apply("Invalid Input!", "bold/Italic/red"))
    return rep


################################################################### 2 Player code ###################################################################


def how_to_play():
    with open("rules.txt", "r") as f:
        contents = f.read()
        print(contents)


if __name__ == "__main__":
    main()
