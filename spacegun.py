import pygame
from pygame.sprite import Sprite


class Gun(Sprite):
    def __init__(self, screen):    # инициализация пушки
        super(Gun, self).__init__()
        self.screen = screen     # получаем экран
        self.image = pygame.image.load('images/pixil-frame-0.png')
        '''получаем поверхность графического объекта(экрана) и
         поверхность самой картинки, чтобы потом их нарисовать
         берем пушку как прямоугольник и графический объект
         как прямоугольник и распогалаем пушку на графическом объекте'''
        self.rect = self.image.get_rect()   # пушка
        self.screen_rect = screen.get_rect()     # экран
        '''координата центра пушки по центру экрана '''
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False  # false пока не нажали на клавишу
        self.mleft = False

    def draw(self):
        '''отрисовываем пушку как объект(прямоугольник'''
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        '''обновление позиции пушки'''
        if self.mright is True and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 2
        elif self.mleft is True and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 2

    def create_gun(self):
        '''размещает пушку по центру внизу'''
        self.center = self.screen_rect.centerx
