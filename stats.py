'''Здесь находится статистика для игры'''
class Stats():
    def __init__(self):
        '''инициализирует статистику'''
        self.reset_stats()
        self.run_game = True
        with open('highscore.txt', 'r') as f:  #режим чтения
            self.high_score = int(f.readline())

    def reset_stats(self):
        '''статистика, изменяющаяся во время игры'''
        self.guns_left = 1  #оставшиеся жизни
        self.score = 0