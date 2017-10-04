                                               BOMBERMAN GAME

TO RUN THE GAME->
  python3 main.py

The code is implemented in 3 files person_bomberman_enemy.py ,bcolors_board.py and main.py .Coding Done mainly in 6 classes Person, Bomberman , Enemy  where class Enemy and class Bomberman are inheriting from class Person and there are also three other classes  Board bcolors and main. All the functions names are self explanatory and give an indication what the function does.

Size of board used  :-> 42*82
Size of object used :-> 2*4
Number of bricks    :-> 25 (can be changed)
Number of enemies   :-> 10 (can be changed)
Number of lives     :-> 5  (can be changed)

-> If all the lives are used then the game is automatically quit and final score is shown .
-> Initally when bomb is placed it is placed on the bomberman position and in first frame instead of bomberman bomb is shown , after pressing any of a,s,w,d bomberman position can be changed and both are shown.
->While a bomb is placed and it's not exploded yet another bomb can't be placed.

6 colors are used:->

Color white and letter 'B' used for Bomberman
Color bue and letter 'X' used for wall
Color yellow and letter 'E' used for enemy
Color green and letter '/' used for brick
Color red and letter 'O' used for bomb
Color purple and letter 'e' used for explosion


To operate the game:

1. Pressing a -> left
2. Pressing d -> right
3. Pressing w -> up
4. Pressing s -> bottom
5. Pressing b -> A bomb is placed
6. Pressing q -> Game is over and the final score is displayed

