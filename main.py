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

running = True
while running:
    dt = clock.tick(FPS) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dx = (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a])
    dy = (keys[pygame.K_DOWN] or keys[pygame.K_s]) - (keys[pygame.K_UP] or keys[pygame.K_w])

    player.x += dx * PLAYER_SPEED * dt
    player.y += dy * PLAYER_SPEED * dt

    if (player.x + PLAYER_SIZE > WIDTH or
        player.x < 0 or
        player.y < 0 or
        player.y + PLAYER_SIZE > HEIGHT):
        running = False

    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, player)
    pygame.display.flip()

pygame.quit()

