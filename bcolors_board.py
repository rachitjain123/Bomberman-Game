"""
    colors and board
"""
import random
class Bcolors():
    """
        Colors class
    """
    def __init__(self):
        pass
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Board():
    """
        Board class
    """
    def __init__(self):
        self.is_game_over = False
        self.create_array()
        self.cord_of_bomberman()
        self.build_walls()
        self.create_bombs()
        self.create_bricks()

    def build_walls(self):
        """
            build walls
        """
        x_buildwall = 0
        for i in range(0, 21):
            self.array[20][i].append('X')
        while True:
            if x_buildwall >= 20:
                break
            cnt = 0
            i = 0
            while True:
                if i >= 21:
                    break
                if cnt >= 4:
                    i = i+2
                    cnt = 0
                    continue
                self.array[x_buildwall][i].append('X')
                cnt = cnt+4
            x_buildwall = x_buildwall+2
        for i in range(0, 21):
            if 'X' not in self.array[0][i]:
                self.array[0][i].append('X')
        for i in range(0, 21):
            if 'X' not in self.array[i][0]:
                self.array[i][0].append('X')
            if 'X' not in self.array[i][20]:
                self.array[i][20].append('X')
    def create_bombs(self):
        """
            create bombs
        """
        self.bombarray = []
        for i in range(0, 21):
            self.bombarray.append([])
            for j in range(0, 21):
                j = j
                self.bombarray[i].append(0)
    def create_array(self):
        """
            create array
        """
        self.array = []
        for i in range(0, 21):
            self.array.append([])
            for j in range(0, 21):
                j = j
                self.array[i].append([' '])
    def print_board(self):
        """
            print board
        """
        for i in range(0, 21):
            print_string = ''
            for j in range(0, 21):
                for k in range(0, 4):
                    k = k
                    if 'E' in self.array[i][j]:
                        print_string = print_string+Bcolors.WARNING+'E'+Bcolors.ENDC
                    elif 'O' in self.array[i][j]:
                        print_string = print_string+Bcolors.FAIL+'O'+Bcolors.ENDC
                    elif 'B' in self.array[i][j]:
                        print_string = print_string+Bcolors.BOLD+'B'+Bcolors.ENDC
                    elif 'X' in self.array[i][j]:
                        print_string = print_string+Bcolors.OKBLUE+'X'+Bcolors.ENDC
                    elif '/' in self.array[i][j]:
                        print_string = print_string+Bcolors.OKGREEN+'/'+Bcolors.ENDC
                    elif 'e' in self.array[i][j]:
                        print_string = print_string+Bcolors.HEADER+'e'+Bcolors.ENDC
                    else:
                        print_string = print_string+' '
            print(print_string)
            print(print_string)


    def cord_of_bomberman(self):
        """
            get coordinates
        """
        self.array[1][1].append('B')

    def create_bricks(self):
        """
            create bricks
        """
        cnt = 0
        x_random = random.randint(3, 19)
        y_random = random.randint(3, 18)
        #change 25 to change the number of bricks
        while cnt < 25:
            while len(self.array[y_random][x_random]) != 1:
                x_random = random.randint(3, 19)
                y_random = random.randint(3, 18)
            self.array[y_random][x_random].append('/')
            cnt = cnt+1
