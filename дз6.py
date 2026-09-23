import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

ball = pygame.Rect(100, 250, 50, 50)

speed = 1

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.x += speed

    if ball.right >= WIDTH:
        speed = -speed

    if ball.left <= 0:
        speed = -speed

    screen.fill((0, 0, 0))
    pygame.draw.ellipse(screen, (255, 255, 255), ball)

    pygame.display.update()

pygame.quit()