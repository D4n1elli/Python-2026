# Number Guessing Game

## How the game works
When running the game, the user is presented with a menu containing four different difficulties, and must choose one to proceed playing. Then, a random number is generated and the goal is to guess it.
The game only helps by saying either:
- Try a higher number
or 
- Try a lower number

After guessing it, the code outputs the number of attempts and a final message.
The user can choose to play again by typing the difficulty they want or decide to stop playing by typing 0.

## Features
The game has 4 different levels:
- Easy (between 1 and 20)
- Medium (between 1 and 100)
- Hard (between 1 and 1000)
- Custom (the user chooses the start and end of the intervail)

Every number the user types goes through validation: if the difficulty chosen is valid, if their guess is inside the interval, or if the start and end on the custom mode is valid.