import pygame, sys
from day2.pathfinding_algos  import main
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)
 
font = pygame.font.SysFont(None, 20)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
 
def main_menu():
    while True:
 
        screen.fill((0,0,0))
        draw_text('Choose Algorithm', font, (255, 255, 255), screen, 20, 20)
 
        mx, my = pygame.mouse.get_pos()

        smallfont = pygame.font.SysFont('Corbel',15)
        color = (255,255,255)
        text = smallfont.render('<------ A Star Algorithm' , True , color)
        text2 = smallfont.render('<------Djikstra Algoritm' , True , color)
 
        button_1 = pygame.Rect(20, 100, 120, 20)
        button_2 = pygame.Rect(20, 200, 220, 20)
        screen.blit(text , (260,100))
        screen.blit(text2 , (260,200))
        if button_1.collidepoint((mx, my)):
            if click:
                WIDTH = 800
                WIN = pygame.display.set_mode((WIDTH, WIDTH))
                main(WIN, WIDTH , 1)
        if button_2.collidepoint((mx, my)):
            if click:
                WIDTH = 800
                WIN = pygame.display.set_mode((WIDTH, WIDTH))
                main(WIN, WIDTH , 2)
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 

main_menu()