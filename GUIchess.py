from os import path

import pygame

import main

img_dir = path.join(path.dirname(__file__), 'img')

WIDTH = 600
HEIGHT = 600
FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
background = pygame.transform.scale(pygame.image.load(path.join(img_dir, "deck.png")).convert_alpha(), (WIDTH, HEIGHT))
background_rect = background.get_rect()
queen = pygame.transform.scale(pygame.image.load(path.join(img_dir, "queen.png")).convert_alpha(),
                               (WIDTH // 8, HEIGHT // 8))
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, background_rect)
    start_x, start_y = 0, 0
    for i in main.finalmatrix:
        start_x = 0
        for j in i:
            if j == 1:
                screen.blit(queen, [start_x, start_y])
            start_x += WIDTH // 8
        start_y += WIDTH // 8
    pygame.display.flip()

pygame.quit()
