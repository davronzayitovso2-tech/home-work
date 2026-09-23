import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('красный квардат')

square = pygame.Rect(100, 100, 50, 50)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), square)

    pygame.display.flip()

pygame.quit()