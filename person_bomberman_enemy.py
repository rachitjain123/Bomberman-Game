"""
    class person bomberman enemy
"""
import random
class Person():
    """
        Person class
    """
    def __init__(self, xcod, ycod):
        self.xcordi = xcod
        self.ycordi = ycod

    def is_able_to_move(self, xcod, ycod, gameob):
        """
            check for moving
        """
        if xcod > 20 or xcod < 0 or ycod > 20 or ycod < 0:
            return False
        if 'X' in gameob.array[ycod][xcod]:
            return False
        if 'E' in gameob.array[ycod][xcod]:
            return False
        if '/' in gameob.array[ycod][xcod]:
            return False
        if 'O' in gameob.array[ycod][xcod]:
            return False
        return True

class Bomberman(Person):
    """
        Bomberman class
    """
    def __init__(self, xcod, ycod):
        Person.__init__(self, xcod, ycod)
        self.score = 0
        self.lives = 5
        # gameob is of Board class
    def check_for_bombs(self, gameob, cur_enemy):
        """
            check bombs
        """
        flag = 1
        for i in range(0, 21):
            for j in range(0, 21):
                if gameob.bombarray[i][j] == 0:
                    continue
                if gameob.bombarray[i][j] == -1:
                    gameob.bombarray[i][j] = 1
                    continue
                gameob.bombarray[i][j] = gameob.bombarray[i][j]+1
                if gameob.bombarray[i][j] >= 4:
                    gameob.bombarray[i][j] = 0
                    gameob.array[i][j].remove('O')
                    for k in range(j-1, j+2):
                        if k < 0 or k > 20:
                            break
                        elif '/' in gameob.array[i][k]:
                            self.score = self.score+20
                            gameob.array[i][k].remove('/')
                            gameob.array[i][k].append('e')
                        elif 'O' in gameob.array[i][k]:
                            gameob.array[i][k].remove('O')
                            gameob.array[i][k].append('e')
                            gameob.bombarray[i][k] = 0
                        elif 'E' in gameob.array[i][k]:
                            self.score = self.score+100
                            for z_move in range(0, len(cur_enemy)):
                                if cur_enemy[z_move].xcordi == k and cur_enemy[z_move].ycordi == i:
                                    cur_enemy.remove(cur_enemy[z_move])
                                    gameob.array[i][k].remove('E')
                                    break
                            gameob.array[i][k].append('e')
                        elif 'B' in gameob.array[i][k]:
                            flag = 0
                            self.lives = self.lives-1
                        else:
                            gameob.array[i][k].append('e')

                    for k in range(i-1, i+2):
                        if k < 0 or k > 20:
                            break
                        elif '/' in gameob.array[k][j]:
                            self.score = self.score+20
                            gameob.array[k][j].remove('/')
                            gameob.array[k][j].append('e')
                        elif 'O' in gameob.array[k][j]:
                            gameob.array[k][j].remove('O')
                            gameob.array[k][j].append('e')
                            gameob.bombarray[k][j] = 0
                        elif 'E' in gameob.array[k][j]:
                            self.score = self.score+100
                            for z_move in range(0, len(cur_enemy)):
                                if cur_enemy[z_move].xcordi == j and cur_enemy[z_move].ycordi == k:
                                    cur_enemy.remove(cur_enemy[z_move])
                                    gameob.array[k][j].remove('E')
                                    break
                            gameob.array[k][j].append('e')
                        elif 'B' in gameob.array[k][j]:
                            if flag == 1:
                                self.lives = self.lives-1
                        else:
                            gameob.array[k][j].append('e')

    def check_for_enemies(self, gameob, cur_enemy):
        """
            check enemies
        """
        if 'E' in gameob.array[self.ycordi][self.xcordi]:
            self.lives = self.lives-1
            for i in range(0, len(cur_enemy)):
                if cur_enemy[i].xcordi == self.xcordi and cur_enemy[i].ycordi == self.ycordi:
                    cur_enemy.remove(cur_enemy[i])
                    gameob.array[self.ycordi][self.xcordi].remove('E')
                    break
        if self.lives == 0:
            gameob.is_game_over = True

    def remove_explosions(self, gameob):
        """
            remove explosions
        """
        for i in range(0, 20):
            for j in range(0, 20):
                if 'e' in gameob.array[i][j]:
                    gameob.array[i][j].remove('e')


    def print_score(self):
        """
            print score
        """
        print("Score : "+str(self.score))
        print("Lives : "+str(self.lives))

    def move_object(self, char, gameob):
        """
            move object
        """
        if char == 'b' or char == 'B':
            flag = 1
            for i in range(0, 21):
                for j in range(0, 21):
                    if gameob.bombarray[i][j] >= 1:
                        flag = 0

            if flag != 0:
                gameob.array[self.ycordi][self.xcordi].append('O')
                gameob.bombarray[self.ycordi][self.xcordi] = -1

        elif char == 'a' or char == 'A':
            if self.is_able_to_move(self.xcordi-1, self.ycordi, gameob):
                gameob.array[self.ycordi][self.xcordi].remove('B')
                gameob.array[self.ycordi][self.xcordi-1].append('B')
                self.xcordi = self.xcordi-1
                self.ycordi = self.ycordi

        elif char == 'w' or char == 'W':
            if self.is_able_to_move(self.xcordi, self.ycordi-1, gameob):
                gameob.array[self.ycordi][self.xcordi].remove('B')
                gameob.array[self.ycordi-1][self.xcordi].append('B')
                self.xcordi = self.xcordi
                self.ycordi = self.ycordi-1

        elif char == 's' or char == 'S':
            if self.is_able_to_move(self.xcordi, self.ycordi+1, gameob):
                gameob.array[self.ycordi][self.xcordi].remove('B')
                gameob.array[self.ycordi+1][self.xcordi].append('B')
                self.xcordi = self.xcordi
                self.ycordi = self.ycordi+1

        elif char == 'd' or char == 'D':
            if self.is_able_to_move(self.xcordi+1, self.ycordi, gameob):
                gameob.array[self.ycordi][self.xcordi].remove('B')
                gameob.array[self.ycordi][self.xcordi+1].append('B')
                self.xcordi = self.xcordi+1
                self.ycordi = self.ycordi

class Enemy(Person):
    """
        enemy class
    """
    def __init__(self, gameob):
        xcod = random.randint(0, 20)
        ycod = random.randint(0, 20)
        while len(gameob.array[ycod][xcod]) != 1:
            xcod = random.randint(0, 20)
            ycod = random.randint(0, 20)
        Person.__init__(self, xcod, ycod)
        gameob.array[ycod][xcod].append('E')

    def random_move_enemy(self, gameob):
        """
            random move enemy
        """
        dict_check = dict()
        flag = 1
        dict_check[1] = 0
        dict_check[2] = 0
        dict_check[3] = 0
        dict_check[4] = 0
        while True:
            flagg = 0
            if dict_check[1] == 1 and dict_check[2] == 1:
                flagg = 1
            if dict_check[3] == 1 and dict_check[4] == 1 and flagg == 1:
                break
            num = random.randint(1, 4)
            if num == 1:
                dict_check[1] = 1
                if self.is_able_to_move(self.xcordi+1, self.ycordi, gameob):
                    gameob.array[self.ycordi][self.xcordi].remove('E')
                    gameob.array[self.ycordi][self.xcordi+1].append('E')
                    self.xcordi = self.xcordi+1
                    self.ycordi = self.ycordi
                    flag = 0

            elif num == 2:
                dict_check[2] = 1
                if self.is_able_to_move(self.xcordi-1, self.ycordi, gameob):
                    gameob.array[self.ycordi][self.xcordi].remove('E')
                    gameob.array[self.ycordi][self.xcordi-1].append('E')
                    self.xcordi = self.xcordi-1
                    self.ycordi = self.ycordi
                    flag = 0

            elif num == 3:
                dict_check[3] = 1
                if self.is_able_to_move(self.xcordi, self.ycordi+1, gameob):
                    gameob.array[self.ycordi][self.xcordi].remove('E')
                    gameob.array[self.ycordi+1][self.xcordi].append('E')
                    self.xcordi = self.xcordi
                    self.ycordi = self.ycordi+1
                    flag = 0

            elif num == 4:
                dict_check[4] = 1
                if self.is_able_to_move(self.xcordi, self.ycordi-1, gameob):
                    gameob.array[self.ycordi][self.xcordi].remove('E')
                    gameob.array[self.ycordi-1][self.xcordi].append('E')
                    self.xcordi = self.xcordi
                    self.ycordi = self.ycordi-1
                    flag = 0

            if flag == 0:
                break
