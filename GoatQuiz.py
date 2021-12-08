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
startSound = pygame.mixer.Sound(os.path.join(sys.path[0], r"Sounds\scream.mp3"))
clickSound = pygame.mixer.Sound(os.path.join(sys.path[0], r"Sounds\click.mp3"))

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
                pygame.mixer.Sound.play(clickSound)
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                action = False
        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        return action

# Creating button instances
startButton = Button(384,570,startButtonImg)
ansbutton1 = Button(50,200,button1)
ansbutton2 = Button(50,290,button2)
ansbutton3 = Button(50,380,button3)
ansbutton4 = Button(50,470,button4)
ansbutton5 = Button(50,560,button5)
ansbutton6 = Button(50,650,button6)

    
# Question class
class Questions():
    def question(text, ans1, goat1, ans2, goat2, ans3, goat3, ans4, goat4, ans5, goat5, ans6, goat6):
        #Rendering text
        questionText = defFont.render(text, True, white)
        ans1Text = defFont.render(ans1, True, white)
        ans2Text = defFont.render(ans2, True, white)
        ans3Text = defFont.render(ans3, True, white)
        ans4Text = defFont.render(ans4, True, white)
        ans5Text = defFont.render(ans5, True, white)
        ans6Text = defFont.render(ans6, True, white)
        #Displaying it on screen
        screen.blit(questionText,(50,50))
        screen.blit(ans1Text,(140,200))
        screen.blit(ans2Text,(140,290))
        screen.blit(ans3Text,(140,380))
        screen.blit(ans4Text,(140,470))
        screen.blit(ans5Text,(140,560))
        screen.blit(ans6Text,(140,650))
        
        #Goat integers
        global happyGoat
        global sadGoat
        global tropicalGoat
        global anxiousGoat
        global gamerGoat
        global angryGoat
        global healthyGoat
        global spiderGoat
        global nomadGoat
        global armyGoat
        global musicalGoat
        global boxerGoat
        
        happyGoat = 0
        sadGoat = 0
        tropicalGoat = 0
        anxiousGoat = 0
        gamerGoat = 0
        angryGoat = 0
        healthyGoat = 0
        spiderGoat = 0
        nomadGoat = 0
        armyGoat = 0
        musicalGoat = 0
        boxerGoat = 0
        
        #Drawing buttons
        if ansbutton1.draw() == True:
            print("Button1")
            #button goes down when pressed
            pygame.draw.rect(screen,navy,pygame.Rect(50,200,80,560))
            screen.blit(button1Down,(50,200))
            screen.blit(button2,(50,290))
            screen.blit(button3,(50,380))
            screen.blit(button4,(50,470))
            screen.blit(button5,(50,560))
            screen.blit(button6,(50,650))
            pygame.display.flip()
            sleep(.1)
            #Goat tally
            if goat1 == "HappyGoat":
                return "HappyGoat"
            elif goat1 == "SadGoat":
                sadGoat = sadGoat + 1
                return sadGoat
            elif goat1 == "TropicalGoat":
                tropicalGoat = tropicalGoat + 1
                return tropicalGoat
            elif goat1 == "AnxiousGoat":
                anxiousGoat = anxiousGoat + 1
                return anxiousGoat
            elif goat1 == "GamerGoat":
                gamerGoat = gamerGoat + 1
                return gamerGoat
            elif goat1 == "AngryGoat":
                angryGoat = angryGoat + 1
                return armyGoat
            elif goat1 == "HealthyGoat":
                healthyGoat = healthyGoat + 1
                return healthyGoat
            elif goat1 == "SpiderGoat":
                spiderGoat = spiderGoat + 1
                return spiderGoat
            elif goat1 == "NomadGoat":
                nomadGoat = nomadGoat + 1
                return nomadGoat
            elif goat1 == "ArmyGoat":
                armyGoat = armyGoat + 1
                return armyGoat
            elif goat1 == "MusicalGoat":
                musicalGoat = musicalGoat + 1
                return musicalGoat
            elif goat1 == "BoxerGoat":
                boxerGoat = boxerGoat + 1
                return boxerGoat
                
        if ansbutton2.draw() == True:
            print("Button2")
            #button goes down when pressed
            pygame.draw.rect(screen,navy,pygame.Rect(50,290,80,560))
            screen.blit(button2Down,(50,290))
            screen.blit(button1,(50,200))
            screen.blit(button3,(50,380))
            screen.blit(button4,(50,470))
            screen.blit(button5,(50,560))
            screen.blit(button6,(50,650))
            pygame.display.flip()
            sleep(.1)
            #Goat tally
            if goat2 == "HappyGoat":
                happyGoat = happyGoat + 1
                return happyGoat
            elif goat2 == "SadGoat":
                sadGoat = sadGoat + 1
                return sadGoat
            elif goat2 == "TropicalGoat":
                tropicalGoat = tropicalGoat + 1
                return tropicalGoat
            elif goat2 == "AnxiousGoat":
                anxiousGoat = anxiousGoat + 1
                return anxiousGoat
            elif goat2 == "GamerGoat":
                gamerGoat = gamerGoat + 1
                return gamerGoat
            elif goat2 == "AngryGoat":
                angryGoat = angryGoat + 1
                return armyGoat
            elif goat2 == "HealthyGoat":
                healthyGoat = healthyGoat + 1
                return healthyGoat
            elif goat2 == "SpiderGoat":
                spiderGoat = spiderGoat + 1
                return spiderGoat
            elif goat2 == "NomadGoat":
                nomadGoat = nomadGoat + 1
                return nomadGoat
            elif goat2 == "ArmyGoat":
                armyGoat = armyGoat + 1
                return armyGoat
            elif goat2 == "MusicalGoat":
                musicalGoat = musicalGoat + 1
                return musicalGoat
            elif goat2 == "BoxerGoat":
                boxerGoat = boxerGoat + 1
                return boxerGoat
        if ansbutton3.draw() == True:
            print("Button3")
            #button goes down when pressed
            pygame.draw.rect(screen,navy,pygame.Rect(50,380,80,560))
            screen.blit(button3Down,(50,380))
            screen.blit(button1,(50,200))
            screen.blit(button2,(50,290))
            screen.blit(button4,(50,470))
            screen.blit(button5,(50,560))
            screen.blit(button6,(50,650))
            pygame.display.flip()
            sleep(.1)
            #Goat tally
            if goat3 == "HappyGoat":
                happyGoat = happyGoat + 1
                return happyGoat
            elif goat3 == "SadGoat":
                sadGoat = sadGoat + 1
                return sadGoat
            elif goat3 == "TropicalGoat":
                tropicalGoat = tropicalGoat + 1
                return tropicalGoat
            elif goat3 == "AnxiousGoat":
                anxiousGoat = anxiousGoat + 1
                return anxiousGoat
            elif goat3 == "GamerGoat":
                gamerGoat = gamerGoat + 1
                return gamerGoat
            elif goat3 == "AngryGoat":
                angryGoat = angryGoat + 1
                return armyGoat
            elif goat3 == "HealthyGoat":
                healthyGoat = healthyGoat + 1
                return healthyGoat
            elif goat3 == "SpiderGoat":
                spiderGoat = spiderGoat + 1
                return spiderGoat
            elif goat3 == "NomadGoat":
                nomadGoat = nomadGoat + 1
                return nomadGoat
            elif goat3 == "ArmyGoat":
                armyGoat = armyGoat + 1
                return armyGoat
            elif goat3 == "MusicalGoat":
                musicalGoat = musicalGoat + 1
                return musicalGoat
            elif goat3 == "BoxerGoat":
                boxerGoat = boxerGoat + 1
                return boxerGoat
        if ansbutton4.draw() == True:
            print("Button4")
            #button goes down when pressed
            pygame.draw.rect(screen,navy,pygame.Rect(50,470,80,560))
            screen.blit(button4Down,(50,470))
            screen.blit(button1,(50,200))
            screen.blit(button2,(50,290))
            screen.blit(button3,(50,380))
            screen.blit(button5,(50,560))
            screen.blit(button6,(50,650))
            pygame.display.flip()
            sleep(.1)
            #Goat tally
            if goat4 == "HappyGoat":
                happyGoat = happyGoat + 1
                return happyGoat
            elif goat4 == "SadGoat":
                sadGoat = sadGoat + 1
                return sadGoat
            elif goat4 == "TropicalGoat":
                tropicalGoat = tropicalGoat + 1
                return tropicalGoat
            elif goat4 == "AnxiousGoat":
                anxiousGoat = anxiousGoat + 1
                return anxiousGoat
            elif goat4 == "GamerGoat":
                gamerGoat = gamerGoat + 1
                return gamerGoat
            elif goat4 == "AngryGoat":
                angryGoat = angryGoat + 1
                return armyGoat
            elif goat4 == "HealthyGoat":
                healthyGoat = healthyGoat + 1
                return healthyGoat
            elif goat4 == "SpiderGoat":
                spiderGoat = spiderGoat + 1
                return spiderGoat
            elif goat4 == "NomadGoat":
                nomadGoat = nomadGoat + 1
                return nomadGoat
            elif goat4 == "ArmyGoat":
                armyGoat = armyGoat + 1
                return armyGoat
            elif goat4 == "MusicalGoat":
                musicalGoat = musicalGoat + 1
                return musicalGoat
            elif goat4 == "BoxerGoat":
                boxerGoat = boxerGoat + 1
                return boxerGoat
        if ansbutton5.draw() == True:
            print("Button5")
            #button goes down when pressed
            pygame.draw.rect(screen,navy,pygame.Rect(50,560,80,560))
            screen.blit(button5Down,(50,560))
            screen.blit(button1,(50,200))
            screen.blit(button2,(50,290))
            screen.blit(button3,(50,380))
            screen.blit(button4,(50,470))
            screen.blit(button6,(50,650))
            pygame.display.flip()
            sleep(.1)
            #Goat tally
            if goat5 == "HappyGoat":
                happyGoat = happyGoat + 1
                return happyGoat
            elif goat5 == "SadGoat":
                sadGoat = sadGoat + 1
                return sadGoat
            elif goat5 == "TropicalGoat":
                tropicalGoat = tropicalGoat + 1
                return tropicalGoat
            elif goat5 == "AnxiousGoat":
                anxiousGoat = anxiousGoat + 1
                return anxiousGoat
            elif goat5 == "GamerGoat":
                gamerGoat = gamerGoat + 1
                return gamerGoat
            elif goat5 == "AngryGoat":
                angryGoat = angryGoat + 1
                return armyGoat
            elif goat5 == "HealthyGoat":
                healthyGoat = healthyGoat + 1
                return healthyGoat
            elif goat5 == "SpiderGoat":
                spiderGoat = spiderGoat + 1
                return spiderGoat
            elif goat5 == "NomadGoat":
                nomadGoat = nomadGoat + 1
                return nomadGoat
            elif goat5 == "ArmyGoat":
                armyGoat = armyGoat + 1
                return armyGoat
            elif goat5 == "MusicalGoat":
                musicalGoat = musicalGoat + 1
                return musicalGoat
            elif goat5 == "BoxerGoat":
                boxerGoat = boxerGoat + 1
                return boxerGoat
        if ansbutton6.draw() == True:
            print("Button6")
            #button goes down when pressed
            pygame.draw.rect(screen,navy,pygame.Rect(50,650,80,560))
            screen.blit(button6Down,(50,650))
            screen.blit(button1,(50,200))
            screen.blit(button2,(50,290))
            screen.blit(button3,(50,380))
            screen.blit(button4,(50,470))
            screen.blit(button5,(50,560))
            pygame.display.flip()
            sleep(.1)
            #Goat tally
            if goat6 == "HappyGoat":
                happyGoat = happyGoat + 1
                return happyGoat
            elif goat6 == "SadGoat":
                sadGoat = sadGoat + 1
                return sadGoat
            elif goat6 == "TropicalGoat":
                tropicalGoat = tropicalGoat + 1
                return tropicalGoat
            elif goat6 == "AnxiousGoat":
                anxiousGoat = anxiousGoat + 1
                return anxiousGoat
            elif goat6 == "GamerGoat":
                gamerGoat = gamerGoat + 1
                return gamerGoat
            elif goat6 == "AngryGoat":
                angryGoat = angryGoat + 1
                return armyGoat
            elif goat6 == "HealthyGoat":
                healthyGoat = healthyGoat + 1
                return healthyGoat
            elif goat6 == "SpiderGoat":
                spiderGoat = spiderGoat + 1
                return spiderGoat
            elif goat6 == "NomadGoat":
                nomadGoat = nomadGoat + 1
                return nomadGoat
            elif goat6 == "ArmyGoat":
                armyGoat = armyGoat + 1
                return armyGoat
            elif goat6 == "MusicalGoat":
                musicalGoat = musicalGoat + 1
                return musicalGoat
            elif goat6 == "BoxerGoat":
                boxerGoat = boxerGoat + 1
                return boxerGoat
            
            
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
        pygame.mixer.Sound.play(clickSound)
        pygame.mixer.Sound.play(startSound)
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

running = True
while running == True:
    
    screen.fill(navy)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
    
    goatResponse = Questions.question("Describe your personality with a food", "Steak", "BoxerGoat", "Lucky Charms", "HappyGoat", "Pineapple", "TropicalGoat", "Coffee", "AnxiousGoat", "Hot Dogs", "SpiderGoat", "McDonalds", "ArmyGoat")
    
    print(goatResponse)
    
    Questions.question("Favourite type of drink", "G-Fuel", "GamerGoat", "Pop", "HappyGoat", "Water", "HealthyGoat", "Tea", "AnxiousGoat", "Energy Drink", "BoxerGoat", "Milk", "ArmyGoat")
    clock.tick(60)
    pygame.display.flip()

print("Quiz Finished")
pygame.quit()