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


# Importing an image 
player_surf = pygame.image.load(PLAYER_IMAGE).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

star_surf = pygame.image.load(STAR_IMAGE).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

meteor_surf = pygame.image.load(METEOR_IMAGE).convert_alpha()
meteor_rect = meteor_surf.get_frect(center = ((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)))


while running:
    # event loop
    for event in pygame.event.get():
        # user clicked X to close the window
        if event.type == pygame.QUIT:
            running = False

    # draw game      
    display_surface.fill("lightblue")
    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    if player_rect.right < WINDOW_WIDTH:
            player_rect.left += 0.2
    display_surface.blit(player_surf, player_rect)

    
    display_surface.blit(meteor_surf, meteor_rect)
    

    # updates the full window
    pygame.display.update()


pygame.quit()