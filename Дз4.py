import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Управляемый квадрат')

square = pygame.Rect(100, 100, 50, 50)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        square.y -= 1
    if keys[pygame.K_s]:
        square.y += 1
    if keys[pygame.K_a]:
        square.x -= 1
    if keys[pygame.K_d]:
        square.x += 1

    # Проверяем границы
    if square.left < 0:
        square.left = 0

    if square.right > WIDTH:
        square.right = WIDTH

    if square.top < 0:
        square.top = 0

    if square.bottom > HEIGHT:
        square.bottom = HEIGHT

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), square)

    pygame.display.flip()

pygame.quit()