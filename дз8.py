import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = pygame.Rect(100, 100, 50, 50)
coin = pygame.Rect(400, 300, 30, 30)

speed = 1
score = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player.y -= speed
    if keys[pygame.K_s]:
        player.y += speed
    if keys[pygame.K_a]:
        player.x -= speed
    if keys[pygame.K_d]:
        player.x += speed

    if player.colliderect(coin):
        score += 1
        print("собарно", score)

        coin.x = random.randint(0, WIDTH - coin.width)
        coin.y = random.randint(0, HEIGHT - coin.height)

    if score >= 10:
        print("победа")
        running = False

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0, 0, 255), player)
    pygame.draw.rect(screen, (255, 255, 0), coin)

    pygame.display.flip()

pygame.quit()