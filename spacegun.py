import pygame
class Gun():
    def __init__(self, screen):    #инициализация пушки
        self.screen = screen     #получаем экран
        self.image = pygame.image.load('images/pixil-frame-0.png')   #загружаем картинку
        '''получаем поверхность графического объекта(экрана) и поверхность самой картинки, чтобы потом их нарисовать
        берем пушку как прямоугольник и графический объект как прямоугольник и распогалаем пушку на графическом объекте'''
        self.rect = self.image.get_rect()   #пушка
        self.screen_rect = screen.get_rect()     #экран
        '''создаем координаты центра и '''
        self.rect.centerx = self.screen_rect.centerx  #координата центра пушки по центру экрана
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False  #false пока не нажали на клавишу
        self.mleft = False
    def output(self):
        '''рисование пушки'''
        self.screen.blit(self.image, self.rect)   #отрисооваем пушку как объект(прямоугольник)
    def update_gun(self):
        '''обновление позиции пушки'''
        if self.mright == True and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 4
        elif self.mleft == True and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 4

