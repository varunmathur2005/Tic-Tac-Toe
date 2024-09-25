# Tic-Tac-Toe

## Overview
Tic-Tac-Toe is a classic and nostalgic game, often played on paper with friends. This project recreates the game using Python and SQL, allowing it to be played through the command line. The goal of the game is to get three of your marks (X or O) in a straight line, either vertically, horizontally, or diagonally.

## Features
- **Command Line Interface**: Play the game through a user-friendly command line interface.
- **Random Character Assignment**: Players are assigned either X or O randomly using the `random` module.
- **Stylized Text**: The `fontstyle` module enhances the game's appearance by changing text fonts and colors.
- **Game Records**: The game stores summaries of past games in both text files and a MySQL database.
- **Multiple Game Modes**: Play against another player or a computer (computer mode is under construction).

## Getting Started
When you start the game, you are greeted with a welcome message and asked to make a choice from the menu:

1. **Start a New Game**: Begins a new round of Tic-Tac-Toe.

   ![New Game](https://github.com/varunmathur2005/Tic-Tac-Toe/assets/130909000/6a2401c8-23dc-4919-b823-349b2891ac8e)
   
2. **View Game Rules**: Displays the rules of the game from a text file (`rules.txt`).

   ![Game Rules](https://github.com/varunmathur2005/Tic-Tac-Toe/assets/130909000/8793074f-8ad5-43d3-8bf2-089146bee643)
   
3. **View Last Game Summary**: Shows the summary of the last game from a text file (`RECORD.TXT`).

   ![Last Game Summary](https://github.com/varunmathur2005/Tic-Tac-Toe/assets/130909000/f5246280-8166-4260-8fea-62c4250b31d7)
   
4. **Load Game Records from Database**: Loads and displays all game records stored in the MySQL database.

   ![Load Records](https://github.com/varunmathur2005/Tic-Tac-Toe/assets/130909000/38d39359-c0c4-413d-b8b0-8b9d614638ce)
   
5. **Exit Game**: Exits the game, thanking the user for playing.

   ![Exit](https://github.com/varunmathur2005/Tic-Tac-Toe/assets/130909000/f484d155-10d4-445c-8763-551d18f1bc71)

## Game Logic
The game logic varies depending on the mode selected:

### Player vs. Player Mode
1. **Character Assignment**: Players are randomly assigned X or O.
2. **Board Setup**: A 3x3 grid is displayed, with positions numbered 1-9.

   ![Board Display](https://github.com/varunmathur2005/Tic-Tac-Toe/assets/130909000/b1a9a11f-e0b7-4411-b151-895bcf21e182)

3. **Game Flow**:
   - Players take turns placing their marks on the board.
   - The game checks for win conditions or ties using the `check_win` function.
   - If a player wins, the game ends; if the board fills up, the game is tied.

   ![Gameplay](https://github.com/varunmathur2005/Tic-Tac-Toe/assets/130909000/572aca2d-12a5-4f45-9d1b-1f6b7b3674e0)

4. **Play Again**: After a game ends, players are asked if they want to play again. The game restarts if they choose "Y"; otherwise, it exits with a thank you message.

### Player vs. Computer Mode
Currently under construction. When selected, the game exits with the message: "Player vs computer mode is currently under construction."

## Modules Used
- **`fontstyle`**: Adds style and color to the text, making the game more visually appealing.
- **`random`**: Assigns characters randomly to players.
- **`sys`**: Handles program exits.
- **`mysql.connector`**: Connects to MySQL to store and retrieve game summaries.
