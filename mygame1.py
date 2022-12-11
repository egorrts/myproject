import pygame
import sys
from spacegun import Gun
from pygame.sprite import Group
from bullet import Bullet
from alien import Ino
def events(screen, gun, bullets):
    '''обработка событий'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # закрываем игру по желанию пользователя
            sys.exit()
        elif event.type == pygame.KEYDOWN:  #обрабатываем события с клавиатуры
            if event.key == pygame.K_d:   #для кнопки вправо
                gun.mright = True
            elif event.key == pygame.K_a:   #для кнопки влево
                gun.mleft = True
            elif event.key == pygame.K_SPACE:  #создаем новую пулю
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)   #добавляем эту пулю в контейнер ullets
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            if event.key == pygame.K_a:
                gun.mleft = False
def update_bullets(inos, bullets):
    '''бновляет позиции пуль'''
    '''метод pygame groupcollide перебирает группы пуль и пришельцев и если они пересекаются(сталкиваются), добавляет их в словарь '''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)   #удаляем из контейнера bullets пулю, если выходит за пределы экр
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)  #оба аргумента true удаляют и пулю и пришельца
def update_inos(gun, inos):
    '''обновляет позицию пришельцев'''
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):  #проверяем столкновение пушки и пришельца
        pygame.QUIT
def create_army(screen, inos):
    '''создание армии пришельцев'''
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width)/ino_width) #вычитаем из ширины экрана две ширины пришельца и делим на ширину пришельца
    ino_height = ino.rect.height
    number_ino_y  = int((800 - 300 - 2 * ino_height)/ino_height)
    '''реализуем движение пришельцев'''
    for j in range(number_ino_y):
        for i in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width*i
            ino.y = ino_height + ino_height * j
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height*j
            inos.add(ino)


def run():
    '''создает окно, задает размеры, пишет название, задает цвет фона в формате RGB'''
    pygame.init()
    screen = pygame.display.set_mode((700,700))
    pygame.display.set_caption("Космические защитники")
    displ_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    create_army(screen, inos)

    while True:
        '''основной цикл программы'''
        events(screen, gun, bullets)
        gun.update_gun()
        screen.fill(displ_color)  # метод fill-заливка фона
        for bullet in bullets.sprites():  # рисуем пули до пушки, чтобы пушка была сверху
            bullet.draw_bullet()
        gun.output()
        inos.draw(screen)
        pygame.display.flip()       #создаем финальный экран после окончания игры
        update_bullets(inos, bullets)
        update_inos(gun, inos)
run()