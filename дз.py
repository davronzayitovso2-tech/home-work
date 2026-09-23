import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('Моя первая игра')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 255))

    pygame.display.flip()

pygame.quit()