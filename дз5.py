import pygame

pygame.init()

WIDTH = 1200
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

car = pygame.Rect(100, 250, 100, 50)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        car.x += 1

    if car.left > WIDTH:
        car.right = 0

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), car)

    pygame.display.update()

pygame.quit()