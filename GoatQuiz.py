#Author: Aidan Kooiman
#Date: 11/26/2021
#FileName: GoatQuiz
#Description: A personality quiz that assigns you one of twelve goats at the end

import pygame

pygame.init()
import webbrowser

#Window Size and colors are delcared here
size = width, height = 1024, 768
center = (512,384)
white = (255,255,255)
gray = (211,211,211)
darkGray = (105,105,105)
blue = (0,0,255)
black = (0,0,0)
navy = (21,76,121)

#Pygame window is loaded here
#Along with width height and mouse variables
screen = pygame.display.set_mode(size)
mouse = pygame.mouse.get_pos()
width = screen.get_width()
height = screen.get_height()

#Sprites are loaded here
startSprite = pygame.image.load(r'T:\BDH-ICS3C1-1\aida4421\Python\GoatTest\Sprites\StartButton.png')
startSprite = pygame.transform.scale(startSprite, (512,512))



#Start of game loop
running = True
while(running == True):
    
    screen.fill(navy)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
    
    screen.blit(startSprite,(center))
    
    pygame.display.update()
            
    