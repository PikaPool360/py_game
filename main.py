import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_COLOUR = (225, 255, 255,)
WALL_COLOUR = (255, 50, 255)
PLAYER_SPEED = 7

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Untitled game")

player = pygame.Rect(35, 40, 40, 40)

walls = [
    # the outer walls
    pygame.Rect(0, 0, 800, 10),
    pygame.Rect(0, 590, 800, 10),
    pygame.Rect(0, 0, 10, 600),
    pygame.Rect(790, 0, 10, 600),
    
    #the maze walls
    pygame.Rect(120, 0, 40, 500),
    pygame.Rect(240, 90, 40, 500),
    pygame.Rect(360, 0, 40, 500),
    pygame.Rect(480, 90, 40, 500),
    pygame.Rect(600, 0, 40, 500),
]

circle = {"center": (715, 100), "radius": 10} # maybe a thingy to collect to beat the level

running = True
while running:
    def move_player(player, walls, dx, dy):
        """Move the player and handle collisions with walls."""
        player.move_ip(dx, dy)
        for wall in walls:
            if player.colliderect(wall):
                player.move_ip(-dx, -dy)
                break
    
    screen.fill((0, 0, 0))
        
    pygame.draw.rect(screen, PLAYER_COLOUR, player)
    pygame.draw.circle(screen, (255,255,51), circle["center"], circle["radius"])
    
    # rendering walls
    for wall in walls:
        pygame.draw.rect(screen, WALL_COLOUR, wall)

    # player movement
    key = pygame.key.get_pressed()

    if key[pygame.K_w] == True:
        move_player(player, walls, 0, -PLAYER_SPEED)
    if key[pygame.K_s] == True:
        move_player(player, walls, 0, PLAYER_SPEED)
    if key[pygame.K_a] == True:
        move_player(player, walls, -PLAYER_SPEED, 0)
    if key[pygame.K_d] == True:
        move_player(player, walls, PLAYER_SPEED, 0)

    # to check when to stop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # refreshing the screen
    pygame.display.flip()
    clock.tick(60)
        

pygame.quit()
