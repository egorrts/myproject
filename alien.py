import pygame

class Ino(pygame.sprite.Sprite):
    '''класс одного пришельца'''
    def __init__(self, screen):
        '''инициализируем и задаем начальную позицию'''
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pixil-frame-0 (1).png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = self.rect.x
        self.y = self.rect.y

    def draw(self):
        '''ывод пришельца на экран'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''перемещает пришельцев'''
        self.y += 0.04
        self.rect.y = self.y
