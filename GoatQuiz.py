#Author: Aidan Kooiman
#Date: 11/26/2021
#FileName: GoatQuiz
#Description: A personality quiz that assigns you one of twelve goats at the end

import pygame

import webbrowser
from time import sleep

pygame.init()
pygame.font.init()

#Various Variables used for the pygame window are declared here
size = width, height = 1024, 768
center = (256,384)
white = (255,255,255)
gray = (211,211,211)
darkGray = (105,105,105)
blue = (0,0,255)
black = (0,0,0)
navy = (21,76,121)
defFont = pygame.font.Font(r'C:\Users\gamer\Desktop\Genie\Python Project\Fonts\munro.ttf', 60)
defFontQuestion = pygame.font.Font(r'C:\Users\gamer\Desktop\Genie\Python Project\Fonts\munro.ttf', 100)

#Pygame window is loaded hereS
#Along with width height and mouse variables
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Goat Quiz")
width = screen.get_width()
height = screen.get_height()
startClicked = False

#Sprites are loaded here
#main menu stuff is loaded here
startButtonImg = pygame.image.load(r'C:\Users\gamer\Desktop\Genie\Python Project\Sprites\StartButton.png')
startButtonImg = pygame.transform.scale(startButtonImg, (272,96))
goatQuizTitle = pygame.image.load(r'C:\Users\gamer\Desktop\Genie\Python Project\Sprites\GoatQuizTitle.png')
goatQuizTitle = pygame.transform.scale(goatQuizTitle, (544, 512))
startButtonDownImg = pygame.image.load(r'C:\Users\gamer\Desktop\Genie\Python Project\Sprites\StartButtonDown.png')
startButtonDownImg = pygame.transform.scale(startButtonDownImg, (272,96))
#quiz buttons are loaded here
button1 = pygame.image.load(r'C:\Users\gamer\Desktop\Genie\Python Project\Sprites\Button1.png')
button1 = pygame.transform.scale(button1,(80,80))
button2 = pygame.image.load(r'C:\Users\gamer\Desktop\Genie\Python Project\Sprites\Button2.png')
button2 = pygame.transform.scale(button2,(80,80))
button3 = pygame.image.load(r'C:\Users\gamer\Desktop\Genie\Python Project\Sprites\Button3.png')
button3 = pygame.transform.scale(button3,(80,80))
button4 = pygame.image.load(r'C:\Users\gamer\Desktop\Genie\Python Project\Sprites\Button4.png')
button4 = pygame.transform.scale(button4,(80,80))
button5 = pygame.image.load(r'C:\Users\gamer\Desktop\Genie\Python Project\Sprites\Button5.png')
button5 = pygame.transform.scale(button5,(80,80))
button6 = pygame.image.load(r'C:\Users\gamer\Desktop\Genie\Python Project\Sprites\Button6.png')
button6 = pygame.transform.scale(button6,(80,80))

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

clock = pygame.time.Clock()
#Start of game loop
mainMenu = True
while(mainMenu == True):
    
    screen.fill(navy)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()
    
    if startButton.draw() == False:
        screen.blit(goatQuizTitle,(240, 64))

    else:
        print("Start")
        screen.fill(navy)
        screen.blit(goatQuizTitle,(240, 64))
        screen.blit(startButtonDownImg,(384,570))
        pygame.display.flip()
        sleep(.1)
        screen.blit(startButtonImg,(384,570))
        pygame.display.flip()
        sleep(.1)
        startClicked = True
        goatQuizSlide = 240
        startButtonSlide = 384
        while True:
            
            screen.fill(navy)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    False
                    
            goatQuizSlide = goatQuizSlide + 8
            screen.blit(goatQuizTitle,(goatQuizSlide, 64))
            
            startButtonSlide = startButtonSlide - 8
            screen.blit(startButtonImg,(startButtonSlide, 570))
            
            if goatQuizSlide > 1050:
                mainMenu = False
                break
            
            clock.tick(60)
            pygame.display.flip()
    
    clock.tick(60)
    pygame.display.flip()

text = defFontQuestion.render("How Much Ram?", False, black)
running = True
while running == True:
    
    screen.fill(navy)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
            
    screen.blit(text,(100, 20))
    screen.blit(button1,(100,150))
    screen.blit(button2,(100,250))
    screen.blit(button3,(100,350))
    screen.blit(button4,(100,450))
    screen.blit(button5,(100,560))
    screen.blit(button6,(100,650))
            
    clock.tick(60)
    pygame.display.flip()

pygame.quit()