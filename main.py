"""
    main class
"""
from __future__ import print_function
import signal
import sys
import tty
import termios
from bcolors_board import Board
from person_bomberman_enemy import Bomberman
from person_bomberman_enemy import Enemy
class GetchUnix():
    """
       input
    """
    def __init__(self):
        pass
    def __call__(self):
        fd_move = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd_move)
        try:
            tty.setraw(sys.stdin.fileno())
            ch_move = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd_move, termios.TCSADRAIN, old_settings)
        return ch_move
class AlarmException(Exception):
    """
        exception
    """
    pass
getch = GetchUnix()

def alarm_handler(_signum, _frame):
    """
		alarm
    """
    raise AlarmException

def input_to(timeout=1):
    """
       input
    """
    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''


def main():
    """
        main class
    """
    current_enemies = []
    current_board = Board()
    current_bomberman = Bomberman(1, 1)
    # Change 10 to change number of enemies
    for i in range(0, 20):
        current_enemies.append(Enemy(current_board))
    while True:
        if current_board.is_game_over or current_bomberman.lives <= 0:
            current_board.print_board()
            print("Game Over: Your score is "+str(current_bomberman.score))
            sys.exit(0)
        current_board.print_board()
        current_bomberman.remove_explosions(current_board)
        current_bomberman.remove_explosions(current_board)
        current_bomberman.print_score()
        inp = input_to()
        if inp == 'q':
            print("Game Over: Your score is "+str(current_bomberman.score))
            sys.exit(0)
        current_bomberman.move_object(inp, current_board)
        current_bomberman.check_for_enemies(current_board, current_enemies)
        current_bomberman.check_for_bombs(current_board, current_enemies)
        for i in range(0, len(current_enemies)):
            current_enemies[i].random_move_enemy(current_board)
        current_bomberman.check_for_enemies(current_board, current_enemies)
if __name__ == "__main__":
    main()
