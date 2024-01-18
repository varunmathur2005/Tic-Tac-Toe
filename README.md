# Tic-Tac-Toe
TIC-TAC-TOE GAME
    #### Description:
    My project is based on a classic game which was an integral part of my childhood, namely ,the tic-tac-toe game.
    A simplistic game usually played using spare paper and pencil with our friends. I have created a copy of the tic-tac-toe game
    in  python and SQL using sys, random, time, datetime, mysql.connector and fontstyle modules. It is playable through the command line.
    The purpose of playing Tic-Tac-Toe is to win by getting 3 of your marks (either X or O) in a straight line.
    The straight line can run diagonally, vertically, or horizontally.

    The fontstyle module is used for adding a lot more personality to the command line by changing the font, color of the commands in the
    command line. This in turn makes the game look more appealing and exciting.
    The random module is used for assigning users their characters randomly.
    The sys module is used for exiting from the program.
<img width="241" alt="image" src="https://github.com/varunmathur2005/Tic-Tac-Toe/assets/130909000/6a2401c8-23dc-4919-b823-349b2891ac8e">


    The game starts of by welcoming the user and asking them to input one the following choices:
    --If the user inputs 1 a new game starts.
    --If the user inputs 2 a text file (rules.txt) which contains the rules of the game is displayed.
    --If the user inputs 3 a text file (RECORD.TXT) which contains the summary of the previous game is displayed.
    --If the user inputs 4 the summaries of the games played which are stored in the mySQL database are loaded.
    --If the user inputs 5 the game exits using sys.exit() and displays a message i.e. thanking the user for playing the game.

        Working / Logic behind the game:
    On selecting new game the user is prompted with a choice of either selecting player v/s player mode or player v/s computer mode.
    IF THE USER INPUTS (1) hence selecting player v/s player mode following is carried out:
    --player 1 and player 2 are randomly assigned either X or O through the character function
    which utilizes the functioning of the random module ( particularly random.choice() function). Now the board is created which is a collection of empty strings (reserved for X and O characters) contained in the list. The first string of the board contains "test" so that we can follow the naming convention of 1 through 9.

    --The board is then displayed using the print_board function which takes board as input and displays the board in the command line as a
    3x3 grid following convention of (1-9). The convention represents each of the squares of the grid (wherein "1" represents the first box
    in row 1 , 2 represents the second box in row 1 ... 9 represents the 3rd box in row 3).

    --Initialization of win conditions:if "0" which represents the game is tied , however this may change to "1" if player1 wins or "2" if player 2 wins.

    --Python first checks whether the board is empty through board_full function which takes board as input and gives false as output if the board has spaces and vice versa. If board_full condition equates to false a while loop is initiated which breaks when either the board is full or player 1 / player 2 has secured the win or if the game has tied.

    --Now python checks whether player 1 or player 2 have won the game using check_win function which takes the character assigned to the player and the board giving output of either True if the player has secured victory or False. After checking the win conditions for the both players. If conditions are met then the game exits changing the win condition to either 1 or 2.

    --Now the players are allowed to move . Player assigned "X" moves first using player_move function which takes char("X" or "O") and board as input and first checks whether the board is not completely occupied. Secondly asks the user to input position (1-9) to place their character on the board. If the position is already occupied it prompts the user otherwise it inputs the users character in the board using place_char function which takes the users character , position , board as input and places the users character on the board at their selected position.

    --Now the win conditions are checked again and player with "O" is allowed to move.

    --The game either ends in a tie or when either player 1 or player 2 win the game.

    --Lastly the game asks the user whether they would like to play again using play_again function. If the users input "Y" or "y" main function is called and the game restarts alternately if the user inputs "N" or "n" the program exits  printing a thank you message.

    IF THE USER INPUTS (2) hence selecting player v/s computer mode following is carried out:
    --The program exits using sys.exit and displays the following statement "Player vs computer mode is currently under construction".
