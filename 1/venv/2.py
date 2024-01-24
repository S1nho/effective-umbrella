import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
width, height = 800, 600

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Spawn Objects")

# Инициализация времени
clock = pygame.time.Clock()

# Класс для объектов
class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.rect = self.image.get_rect(center=(x, y))

# Группы спрайтов
all_sprites = pygame.sprite.Group()
left_objects = pygame.sprite.Group()
right_objects = pygame.sprite.Group()

# Функция для создания объектов на заданных координатах
def spawn_objects(side):
    x_positions = [50, 100, 150] if side == "left" else [width - 50, width - 100, width - 150]
    y_positions = [random.randint(50, height - 50) for _ in range(3)]

    for x, y in zip(x_positions, y_positions):
        obj = GameObject(x, y, white)
        all_sprites.add(obj)
        if side == "left":
            left_objects.add(obj)
        else:
            right_objects.add(obj)

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    # Очистка экрана
    screen.fill(black)

    # Создание объектов на левой и правой сторонах
    spawn_objects("left")
    spawn_objects("right")

    # Обновление и отрисовка спрайтов
    all_sprites.update()
    all_sprites.draw(screen)

    # Обновление дисплея
    pygame.display.flip()

    # Задержка для контроля частоты обновления
    clock.tick(60)
