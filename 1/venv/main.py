import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1920, 1080))#flags=pygame.NONFRAME
pygame.display.set_caption("ССПДД")#two.s.pa.two.da
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

# movement
walk_f = [
    pygame.image.load('images/forward_player/forward_player0.png'),
    pygame.image.load('images/forward_player/forward_player1.png'),
    pygame.image.load('images/forward_player/forward_player0.png'),
    pygame.image.load('images/forward_player/forward_player2.png'),
]   
walk_b = [
    pygame.image.load('images/backward_player/backward_player0.png'),
    pygame.image.load('images/backward_player/backward_player1.png'),
    pygame.image.load('images/backward_player/backward_player0.png'),
    pygame.image.load('images/backward_player/backward_player2.png'),
] 
walk_l = [
    pygame.image.load('images/left_player/left_player0.png'),
    pygame.image.load('images/left_player/left_player1.png'),
    pygame.image.load('images/left_player/left_player0.png'),
    pygame.image.load('images/left_player/left_player2.png'),
] 
walk_r = [
    pygame.image.load('images/right_player/right_player0.png'),
    pygame.image.load('images/right_player/right_player1.png'),
    pygame.image.load('images/right_player/right_player0.png'),
    pygame.image.load('images/right_player/right_player2.png'),
] 

player_anim_count = 0
player_speed = 50
player_x = 300
player_y = 500
static = pygame.image.load('images/forward_player/forward_player0.png')


bg = pygame.image.load('images/background.png')


#running = True
while True:
    screen.blit(bg, (0, 0))
    bg.blit(static,  (player_x, player_y))
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        screen.blit(walk_r[player_anim_count], (player_x, player_y))
    elif keys[pygame.K_w]:
        screen.blit(walk_f[player_anim_count], (player_x, player_y))
    elif keys[pygame.K_s]:
        screen.blit(walk_b[player_anim_count], (player_x, player_y))
    elif keys[pygame.K_a]:
        screen.blit(walk_l[player_anim_count], (player_x, player_y))

    if keys[pygame.K_d] and player_x < 1760:
        player_x += player_speed
    elif keys[pygame.K_a]and player_x > 60:    
        player_x -= player_speed
    elif keys[pygame.K_w]and player_y > 60:
        player_y -= player_speed
    elif keys[pygame.K_s]and player_y < 920:
        player_y += player_speed
    
    
    if player_anim_count == 3:
        player_anim_count = 0
    else:    
        player_anim_count += 1

    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
            pygame.quit()
    
    clock.tick(10)
