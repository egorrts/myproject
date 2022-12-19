import pygame
import sys
from spacegun import Gun
from pygame.sprite import Group
from bullet import Bullet
from alien import Ino
from stats import Stats
import time
from scores import Scores


def handle_events(screen, gun, bullets):
    '''обработка событий'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # закрываем игру по желанию пользователя
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # обрабатываем события с клавиатуры
            if event.key == pygame.K_d:   # для кнопки вправо
                gun.mright = True
            elif event.key == pygame.K_a:   # для кнопки влево
                gun.mleft = True
            elif event.key == pygame.K_SPACE:  # создаем новую пулю
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)  # добавляем пулю в контейнер ullets
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.mright = False
            if event.key == pygame.K_a:
                gun.mleft = False


def update_bullets(screen, stats, sc, inos, bullets):
    '''бновляет позиции пуль'''
    '''метод pygame groupcollide перебирает группы пуль и пришельцев и если они
     пересекаются(сталкиваются), добавляет их в словарь '''
    bullets.update()
    '''удаляем из bullets пулю, если выходит за экр'''
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    '''оба аргумента true удаляют и пулю и пришельца'''
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():
            stats.score += 10 * len(inos)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)


def gun_kill(stats, screen, sc, gun, inos, bullets):
    '''столкновение пушки и армии'''
    if stats.guns_left > 0:
        stats.guns_left -= 1
        sc.image_guns()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def update_inos(stats, screen, sc, gun, inos, bullets):
    '''обновляет позицию пришельцев'''
    inos.update()
    '''проверяем столкновение пушки и пришельца с помощью метода colledeany'''
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, sc, gun, inos, bullets)
    inos_check(stats, screen, sc, gun, inos, bullets)


def inos_check(stats, screen, sc, gun, inos, bullets):
    '''проверка, добралась ли армия до края экрана'''
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc,  gun, inos, bullets)
            break


def create_army(screen, inos):
    '''создание армии пришельцев'''
    ino = Ino(screen)
    ino_width = ino.rect.width
    '''вычитаем из шир экрана 2 шир пришельца и делим на ширину пришельца'''
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((500 - 2 * ino_height) / ino_height)
    '''реализуем движение пришельцев'''
    for j in range(number_ino_y):
        for i in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width*i
            ino.y = ino_height + ino_height * j
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height*j
            inos.add(ino)


def check_high_score(stats, sc):
    '''проверка новых рекордов'''
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:  # режим редактирования
            f.write(str(stats.high_score))


def run():
    '''создает окно, задает размеры, пишет название,
    задает цвет фона в формате RGB'''
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Космические защитники")
    displ_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        '''основной цикл программы'''
        handle_events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            screen.fill(displ_color)
            sc.show_score()
            for bullet in bullets.sprites():
                bullet.draw()
            gun.draw()
            inos.draw(screen)
            pygame.display.flip()
            update_bullets(screen, stats, sc, inos, bullets)
            update_inos(stats, screen, sc,  gun, inos, bullets)


run()
