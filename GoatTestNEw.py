#Author: Aidan Kooiman
#Date: 11/24/2021
#filename: GoatTest
#description: 

import pygame
import webbrowser

pygame.init()
pygame.mixer.quit()

def open():
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=nlYlNF30bVg")
    

size = width, height = 1024, 768
background = pygame.Surface((1024, 768))
center = (360,240)
white = (255,255,255)
gray = (211,211,211)
darkGray = (105,105,105)
blue = (0,0,255)
black = (0,0,0)

screen = pygame.display.set_mode(size)
mouse = pygame.mouse.get_pos()
width = screen.get_width()
height = screen.get_height()




running = True
while(running == True):
    
    screen.fill(darkGray)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        open()
    
    pygame.draw.rect(screen,black,(400,500,400,500))
        
    pygame.display.update()
            


pygame.quit()  
