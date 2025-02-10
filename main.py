import pygame
from settings import *
from random import randint

# general setup 
pygame.init()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) 
pygame.display.set_caption(TITLE)
# when the game is running 
running = True

# Plain Surface
surf = pygame.Surface((100,200))
x = 100

star = pygame.Surface((300, 200))


# Importing an image 
player_surf = pygame.image.load(PLAYER_IMAGE).convert_alpha()
star_surf = pygame.image.load(STAR_IMG).convert_alpha()

while running:
    # event loop
    for event in pygame.event.get():
        # user clicked X to close the window
        if event.type == pygame.QUIT:
            running = False

    # draw game      
    display_surface.fill("darkgrey")
    x += 0.1
    display_surface.blit(player_surf, (x,150))
    for _ in range(20):
        display_surface.blit(star_surf,(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))

    # updates the full window
    pygame.display.update()
        # Limits FPS to 60


pygame.quit()