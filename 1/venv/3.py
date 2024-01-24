import pygame
import random

from pygame.sprite import AbstractGroup

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1280, 720))#flags=pygame.NONFRAME
pygame.display.set_caption("ССПДД")#two.s.pa.two.da
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)


bg = pygame.image.load('images/background.png')

# Описываем свойства и методы для работы с любым будущим персонажем
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load('images/forward_player/forward_player0.png')
        self.rect = self.surf.get_rect()
    
    # Все обработки перемещений оставляем тут, в тч выход за пределы экрана
    def update(self, pressed_keys):
        if pressed_keys[pygame.K_d]:
            self.surf = pygame.image.load('images/right_player/right_player0.png')
            self.rect.move_ip(50, 0)
        if pressed_keys[pygame.K_w]:
            self.surf = pygame.image.load('images/forward_player/forward_player0.png')
            self.rect.move_ip(0, -50)
        if pressed_keys[pygame.K_s]:
            self.surf = pygame.image.load('images/backward_player/backward_player0.png')
            self.rect.move_ip(0, 50)
        if pressed_keys[pygame.K_a]:
            self.surf = pygame.image.load('images/left_player/left_player0.png')
            self.rect.move_ip(-50, 0)

class Car(pygame.sprite.Sprite):    
    def __init__(self):
        super().__init__()
        self.speed = random.randint(70,140)
        self.c_r = pygame.image.load('images/cars_r/blackcarr.png'),
        self.c_l = pygame.image.load('images/cars_l/blackcarl.png'),
        self.r_u = ((1500,145),self.c_r)
        self.r_d = ((1500,240),self.c_r)
        self.l_u = ((-200,415),self.c_l)
        self.l_d = ((-200,510),self.c_l)
        self.dirs = (self.l_u,self.l_d,self.r_u,self.r_d)
        self.dir = random.choice(self.dirs)
# инициализируем первого персонажа по образу и подобию нашего Player
policeman = Player()

#running = True
while True:
    
    keys = pygame.key.get_pressed()

    # Делегируем обработку действий самому персонажу
    policeman.update(keys)

    # Ререндерим не только челика, но и бэкграунд
    screen.blit(bg, (0, 0))
    screen.blit(policeman.surf, policeman.rect)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
            pygame.quit()
    
    clock.tick(10)
