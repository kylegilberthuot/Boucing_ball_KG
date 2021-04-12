import pygame, sys
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS

pygame.init()
surface = pygame.display.set_mode((300,400))

current_y = 100
dy = 2

def drawBall():
    pygame.draw.circle(surface, (0,255,0), (150, int(current_y)), 12)

while True:
    surface.fill((0,0,0))
    current_y += dy
    drawBall()

    print(current_y)
    if current_y > 376 or current_y < 10:
        dy*=-1
    pygame.display.update()

    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit
