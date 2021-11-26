#Author: Aidan Kooiman
#Date: 11/26/2021
#FileName: GoatQuiz
#Description: A personality quiz that assigns you one of twelve goats at the end

import pygame

pygame.init()
import webbrowser

#Window Size and colors are delcared here
size = width, height = 1024, 768
center = (256,384)
white = (255,255,255)
gray = (211,211,211)
darkGray = (105,105,105)
blue = (0,0,255)
black = (0,0,0)
navy = (21,76,121)

#Pygame window is loaded here
#Along with width height and mouse variables
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Goat Quiz")
width = screen.get_width()
height = screen.get_height()

#Sprites are loaded here
startButtonImg = pygame.image.load(r'T:\BDH-ICS3C1-1\aida4421\Python\GoatTest\Sprites\StartButton.png')
startButtonImg = pygame.transform.scale(startButtonImg, (272,96))
goatQuizTitle = pygame.image.load(r'T:\BDH-ICS3C1-1\aida4421\Python\GoatTest\Sprites\GoatQuizTitle.png')
goatQuizTitle = pygame.transform.scale(goatQuizTitle, (544, 512))
startButtonDownImg = pygame.image.load(r'T:\BDH-ICS3C1-1\aida4421\Python\GoatTest\Sprites\StartButtonDown.png')
startButtonDownImg = pygame.transform.scale(startButtonDownImg, (272,96))
#button class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x , y)
        self.clicked = False
    
    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        #check if mouse is on button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        return action

#creating button instances
startButton = Button(384,570,startButtonImg)


#Start of game loop
running = True
while(running == True):
    
    screen.fill(navy)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
    
    if startButton.draw() == True:
        print("Start")
        startButton = Button(384,570,startButtonDownImg)
    else:
        startButton = Button(384,570,startButtonImg)
    screen.blit(goatQuizTitle,(240, 64))
    
    pygame.display.update()

pygame.quit()
    