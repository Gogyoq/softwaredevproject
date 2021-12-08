# Author: Aidan Kooiman, Izaan Syed, Robert Connors, Evan Miller
# Date: 11/26/2021
# FileName: GoatQuiz
# Description: A personality quiz that assigns you one of twelve goats at the end

import pygame

import os
import sys
import webbrowser
from time import sleep

pygame.init()
pygame.font.init()

# Various variables used for the pygame window are declared here
size = width, height = 1024, 768
center = (256,384)
white = (255,255,255)
gray = (211,211,211)
darkGray = (105,105,105)
blue = (0,0,255)
black = (0,0,0)
navy = (21,76,121)

# Pygame window loaded
# Along with width height and mouse variables
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Goat Quiz")
width = screen.get_width()
height = screen.get_height()
startClicked = False

# Getting current directory
cwd = os.getcwd()
print(cwd)

# Main menu assets loading
buttonClickSound = pygame.mixer.Sound(os.path.join(sys.path[0], r"Sounds\click.mp3"))



defFont = pygame.font.Font(os.path.join(sys.path[0], r"Fonts\munro.ttf"), 60)
defFontQuestion = pygame.font.Font(os.path.join(sys.path[0], r"Fonts\munro.ttf"), 60)

startButtonImg = pygame.image.load(os.path.join(sys.path[0], r"Sprites\StartButton.png"), "r")
startButtonImg = pygame.transform.scale(startButtonImg, (272,96))

goatQuizTitle = pygame.image.load(os.path.join(sys.path[0], r"Sprites\GoatQuizTitle.png"), "r")
goatQuizTitle = pygame.transform.scale(goatQuizTitle, (544, 512))
startButtonDownImg = pygame.image.load(os.path.join(sys.path[0], r"Sprites\StartButtonDown.png"), "r")
startButtonDownImg = pygame.transform.scale(startButtonDownImg, (272,96))

# Quiz buttons initialization
button1 = pygame.image.load(os.path.join(sys.path[0], r"Sprites\Button1.png"), "r")
button1 = pygame.transform.scale(button1,(80,80))
button2 = pygame.image.load(os.path.join(sys.path[0], r"Sprites\Button2.png"), "r")
button2 = pygame.transform.scale(button2,(80,80))
button3 = pygame.image.load(os.path.join(sys.path[0], r"Sprites\Button3.png"), "r")
button3 = pygame.transform.scale(button3,(80,80))
button4 = pygame.image.load(os.path.join(sys.path[0], r"Sprites\Button4.png"), "r")
button4 = pygame.transform.scale(button4,(80,80))
button5 = pygame.image.load(os.path.join(sys.path[0], r"Sprites\Button5.png"), "r")
button5 = pygame.transform.scale(button5,(80,80))
button6 = pygame.image.load(os.path.join(sys.path[0], r"Sprites\Button6.png"), "r")
button6 = pygame.transform.scale(button6,(80,80))

# Pressed down version of each button
button1Down = pygame.image.load(os.path.join(sys.path[0], r"Sprites\Button1Down.png"), "r")
button1Down = pygame.transform.scale(button1Down,(80,80))
button2Down = pygame.image.load(os.path.join(sys.path[0], r"Sprites\Button2Down.png"), "r")
button2Down = pygame.transform.scale(button2Down,(80,80))
button3Down = pygame.image.load(os.path.join(sys.path[0], r"Sprites\Button3Down.png"), "r")
button3Down = pygame.transform.scale(button3Down,(80,80))
button4Down = pygame.image.load(os.path.join(sys.path[0], r"Sprites\Button4Down.png"), "r")
button4Down = pygame.transform.scale(button4Down,(80,80))
button5Down = pygame.image.load(os.path.join(sys.path[0], r"Sprites\Button5Down.png"), "r")
button5Down = pygame.transform.scale(button5Down,(80,80))
button6Down = pygame.image.load(os.path.join(sys.path[0], r"Sprites\Button6Down.png"), "r")
button6Down= pygame.transform.scale(button6Down,(80,80))

# Button Class
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

# Creating button instances
startButton = Button(384,570,startButtonImg)

# Question class
class Questions():
    def question1(self, text, ans1, goat1, ans2, goat2, ans3, goat3, ans4, goat4, ans5, goat5, ans6, goat6):
        #Loading question text onto screen
        self.text = text
        screen.blit(text,(50, 50))
        
        # Loading buttons onto screen
        screen.blit(button2,(50,290))
        screen.blit(button3,(50,380))
        screen.blit(button4,(50,470))
        screen.blit(button5,(50,560))
        screen.blit(button6,(50,650))

        # Creating answer button instances
        ansbutton1 = Button(50,200,button1)
        ansbutton2 = Button(50,290,button2)
        ansbutton3 = Button(50,380,button3)
        ansbutton4 = Button(50,470,button4)
        ansbutton5 = Button(50,560,button5)
        ansbutton6 = Button(50,650,button6)

clock = pygame.time.Clock()

# <-- Start of game loop --> 
mainMenu = True
while(mainMenu == True):
    
    screen.fill(navy)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()
    
    if startButton.draw() == False:
        screen.blit(goatQuizTitle,(240, 64))

    else:
        print("Starting Quiz")
        pygame.mixer.Sound.play(buttonClickSound)
        screen.fill(navy)
        screen.blit(goatQuizTitle,(240, 64))
        screen.blit(startButtonDownImg,(384,570))
        pygame.display.flip()
        sleep(.1)
        screen.blit(startButtonImg,(384,570))
        pygame.display.flip()
        sleep(.1)
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

textone = defFontQuestion.render("Describe your personality with a food", False, white)
running = True
while running == True:
    
    screen.fill(navy)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
    
            
    clock.tick(60)
    pygame.display.flip()

print("Quiz Finished")
pygame.quit()