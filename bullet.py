import pygame
'''создаем новый класс на основе класса, который есть в модуле sprite'''


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, gun):
        '''создае  пулю в текущей позиции пушки'''
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 12)  # координаты пули, ширина, выс
        self.color = 139, 195, 74
        self.speed = 8
        self.rect.centerx = gun.rect.centerx  # пуля появля в верх части пушки
        self.rect.top = gun.rect.top

    def update(self):
        '''перемещение пули вверх'''
        self.rect.y -= self.speed

    def draw(self):
        '''рисуем пулю на экране'''
        pygame.draw.rect(self.screen, self.color, self.rect)
