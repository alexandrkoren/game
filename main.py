import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Дивжущийся квадрат')
clock = pygame.time.Clock()

player = pygame.Rect(
    (WIDTH - PLAYER_SIZE) // 2,
    (HEIGHT - PLAYER_SIZE) // 2,
    PLAYER_SIZE,
    PLAYER_SIZE
)

boost_cnt = 50
boost_rect = pygame.Rect(
    WIDTH - 20,
    10,
    10,
    boost_cnt
)

running = True
while running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()
    dx = (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a])
    dy = (keys[pygame.K_DOWN] or keys[pygame.K_s]) - (keys[pygame.K_UP] or keys[pygame.K_w])
    if (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]) and boost_cnt > 0:
        current_speed = BOOST_SPEED
        boost_cnt -= 1
        boost_rect.height = boost_cnt
    else:
        current_speed = PLAYER_SPEED
        boost_cnt += 1
        boost_rect.height = boost_cnt

    player.x += dx * current_speed * dt
    player.y += dy * current_speed * dt

    if (player.x + PLAYER_SIZE > WIDTH or
        player.x < 0 or
        player.y < 0 or
        player.y + PLAYER_SIZE > HEIGHT):
        running = False

    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, (40, 200, 70), boost_rect)
    pygame.display.flip()

pygame.quit()

