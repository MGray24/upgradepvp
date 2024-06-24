import pygame

#initialize pygame, setting up clock/FPS
pygame.init()
clock = pygame.time.Clock()
FPS = 60

#define and create the window
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

#main loop
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.flip()