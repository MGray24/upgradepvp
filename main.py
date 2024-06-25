import pygame
import sys

# initialize pygame, setting up clock/FPS
pygame.init()

click = False


def main_menu():
    global click

    # setting up clock/FPS
    clock = pygame.time.Clock()
    FPS = 60

    # define and create the window
    WIDTH, HEIGHT = 1000, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    running = True

    # main loop
    while running:
        clock.tick(FPS)

        screen.fill('black')

        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(400, 100, 200, 50)
        button_2 = pygame.Rect(400, 200, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

            pygame.display.flip()


pygame.quit()


def game():

    WIDTH, HEIGHT = 1000, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    screen.fill('black')
    running = True
    while running:
        pygame.draw.line(screen, 'white', (0, HEIGHT/2), (WIDTH, HEIGHT / 2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.flip()

def options():

    WIDTH, HEIGHT = 1000, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    screen.fill('black')

    running = True
    while running:
        pygame.draw.line(screen, 'white', (WIDTH / 2, 0), (WIDTH/2, HEIGHT))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.flip()

main_menu()
