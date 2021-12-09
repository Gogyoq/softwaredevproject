# Author: Aidan Kooiman, Izaan Syed, Robert Connors, Evan Miller
# Date: 11/26/2021
# FileName: GoatQuiz
# Description: A personality quiz that assigns you one of twelve goats at the end
# Prerequesites: OpenCV, pygame

import os
import sys
from time import sleep

try:
    import pygame
except:
    print("pygame Not Installed! Please run prerequesite batch file to install.")
    exit()

try:
    import cv2
except:
    print("openCV Not Installed! Please run prerequesite batch file to install.")
    exit()

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

# # Getting current directory
# cwd = os.getcwd()
# print(cwd)

def playvideo(pathVideo):
    video = cv2.VideoCapture(pathVideo)
    success, video_image = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)

    window = pygame.display.set_mode(video_image.shape[1::-1])
    clock = pygame.time.Clock()

    run = success
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        success, video_image = video.read()
        if success:
            video_surf = pygame.image.frombuffer(
                video_image.tobytes(), video_image.shape[1::-1], "BGR")
        else:
            run = False
        window.blit(video_surf, (0, 0))
        pygame.display.flip()

# sound = pygame.mixer.Sound(os.path.join(sys.path[0], r"Sounds\swiftgoat.mp3"))
# pygame.mixer.Sound.play(sound)

# playvideo(os.path.join(sys.path[0], r"Videos\swiftgoatvideo.mp4"))

# <-- Main menu assets loading -->

try:
    backgroundMusic = pygame.mixer.music.load(os.path.join(sys.path[0], r"Sounds\swiftgoat.mp3"))

    startSound = pygame.mixer.Sound(os.path.join(sys.path[0], r"Sounds\scream.mp3"))
    clickSound = pygame.mixer.Sound(os.path.join(sys.path[0], r"Sounds\yoshi.mp3"))

    defFont = pygame.font.Font(os.path.join(sys.path[0], r"Fonts\munro.ttf"), 60)
    defFontQuestion = pygame.font.Font(os.path.join(sys.path[0], r"Fonts\munro.ttf"), 60)

    startButtonImg = pygame.image.load(os.path.join(sys.path[0], r"Sprites\StartButton.png"), "r")
    startButtonImg = pygame.transform.scale(startButtonImg, (272,96))

    goatQuizTitle = pygame.image.load(os.path.join(sys.path[0], r"Sprites\GoatQuizTitle.png"), "r")
    goatQuizTitle = pygame.transform.scale(goatQuizTitle, (544, 512))

    startButtonDownImg = pygame.image.load(os.path.join(sys.path[0], r"Sprites\StartButtonDown.png"), "r")
    startButtonDownImg = pygame.transform.scale(startButtonDownImg, (272,96))

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
    button6Down = pygame.transform.scale(button6Down,(80,80))
except:
    print("Program files are unable to be loaded. Please reinstall.")

#Goat Guy Images and variables
goatGuyNormal = pygame.image.load(os.path.join(sys.path[0], r"Sprites\GoatGuyNormal.png"), "r")
goatGuyNormal = pygame.transform.scale(goatGuyNormal,(320,320))
goatGuyShocked = pygame.image.load(os.path.join(sys.path[0], r"Sprites\GoatGuyShocked.png"), "r")
goatGuyShocked = pygame.transform.scale(goatGuyShocked,(320,320))
goatGuyAngry = pygame.image.load(os.path.join(sys.path[0], r"Sprites\GoatGuyAngry.png"), "r")
goatGuyAngry = pygame.transform.scale(goatGuyAngry,(320,320))
titleButtonCounter = 0
goatGuySlide = -210
loopOnce = 1
goatQuizSlide2 = 64
startButtonSlide2 = 570

# Button Class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x , y)
        self.clicked = False
    
    def draw(self):
        action = False
        # Get mouse position
        pos = pygame.mouse.get_pos()
        # Check if mouse is on button
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                pygame.mixer.Sound.play(clickSound)
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
                action = False
        # Draw button on screen
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
titleButton = Button(240,64,goatQuizTitle)

# Declaring Goat integers
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
    
# Question class
class Questions():
    def question(text, ans1, goat1, ans2, goat2, ans3, goat3, ans4, goat4, ans5, goat5, ans6, goat6):
        # Rendering text
        questionText = defFont.render(text, True, white)
        ans1Text = defFont.render(ans1, True, white)
        ans2Text = defFont.render(ans2, True, white)
        ans3Text = defFont.render(ans3, True, white)
        ans4Text = defFont.render(ans4, True, white)
        ans5Text = defFont.render(ans5, True, white)
        ans6Text = defFont.render(ans6, True, white)
        # Displaying it on screen
        screen.blit(questionText,(50,50))
        screen.blit(ans1Text,(140,200))
        screen.blit(ans2Text,(140,290))
        screen.blit(ans3Text,(140,380))
        screen.blit(ans4Text,(140,470))
        screen.blit(ans5Text,(140,560))
        screen.blit(ans6Text,(140,650))
        
        # Drawing buttons
        if ansbutton1.draw() == True:
            print("Button1")
            # Button goes down when pressed
            pygame.draw.rect(screen,navy,pygame.Rect(50,200,80,560))
            screen.blit(button1Down,(50,200))
            screen.blit(button2,(50,290))
            screen.blit(button3,(50,380))
            screen.blit(button4,(50,470))
            screen.blit(button5,(50,560))
            screen.blit(button6,(50,650))
            pygame.display.flip()
            sleep(.1)
            # Goat tally
            if goat1 == "HappyGoat":
                return "HappyGoat"
            elif goat1 == "SadGoat":
                return "SadGoat"
            elif goat1 == "TropicalGoat":
                return "TropicalGoat"
            elif goat1 == "AnxiousGoat":
                return "AnxiousGoat"
            elif goat1 == "GamerGoat":
                return "GamerGoat"
            elif goat1 == "AngryGoat":
                return "ArmyGoat"
            elif goat1 == "HealthyGoat":
                return "HealthyGoat"
            elif goat1 == "SpiderGoat":
                return "SpiderGoat"
            elif goat1 == "NomadGoat":
                return "NomadGoat"
            elif goat1 == "ArmyGoat":
                return "ArmyGoat"
            elif goat1 == "MusicalGoat":
                return "MusicalGoat"
            elif goat1 == "BoxerGoat":
                return "BoxerGoat"
                
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
                return "HappyGoat"
            elif goat2 == "SadGoat":
                return "SadGoat"
            elif goat2 == "TropicalGoat":
                return "TropicalGoat"
            elif goat2 == "AnxiousGoat":
                return "AnxiousGoat"
            elif goat2 == "GamerGoat":
                return "GamerGoat"
            elif goat2 == "AngryGoat":
                return "ArmyGoat"
            elif goat2 == "HealthyGoat":
                return "HealthyGoat"
            elif goat2 == "SpiderGoat":
                return "SpiderGoat"
            elif goat2 == "NomadGoat":
                return "NomadGoat"
            elif goat2 == "ArmyGoat":
                return "ArmyGoat"
            elif goat2 == "MusicalGoat":
                return "MusicalGoat"
            elif goat2 == "BoxerGoat":
                return "BoxerGoat"

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
                return "HappyGoat"
            elif goat3 == "SadGoat":
                return "SadGoat"
            elif goat3 == "TropicalGoat":
                return "TropicalGoat"
            elif goat3 == "AnxiousGoat":
                return "AnxiousGoat"
            elif goat3 == "GamerGoat":
                return "GamerGoat"
            elif goat3 == "AngryGoat":
                return "ArmyGoat"
            elif goat3 == "HealthyGoat":
                return "HealthyGoat"
            elif goat3 == "SpiderGoat":
                return "SpiderGoat"
            elif goat3 == "NomadGoat":
                return "NomadGoat"
            elif goat3 == "ArmyGoat":
                return "ArmyGoat"
            elif goat3 == "MusicalGoat":
                return "MusicalGoat"
            elif goat3 == "BoxerGoat":
                return "BoxerGoat"

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
                return "HappyGoat"
            elif goat4 == "SadGoat":
                return "SadGoat"
            elif goat4 == "TropicalGoat":
                return "TropicalGoat"
            elif goat4 == "AnxiousGoat":
                return "AnxiousGoat"
            elif goat4 == "GamerGoat":
                return "GamerGoat"
            elif goat4 == "AngryGoat":
                return "ArmyGoat"
            elif goat4 == "HealthyGoat":
                return "HealthyGoat"
            elif goat4 == "SpiderGoat":
                return "SpiderGoat"
            elif goat4 == "NomadGoat":
                return "NomadGoat"
            elif goat4 == "ArmyGoat":
                return "ArmyGoat"
            elif goat4 == "MusicalGoat":
                return "MusicalGoat"
            elif goat4 == "BoxerGoat":
                return "BoxerGoat"

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
                return "HappyGoat"
            elif goat5 == "SadGoat":
                return "SadGoat"
            elif goat5 == "TropicalGoat":
                return "TropicalGoat"
            elif goat5 == "AnxiousGoat":
                return "AnxiousGoat"
            elif goat5 == "GamerGoat":
                return "GamerGoat"
            elif goat5 == "AngryGoat":
                return "ArmyGoat"
            elif goat5 == "HealthyGoat":
                return "HealthyGoat"
            elif goat5 == "SpiderGoat":
                return "SpiderGoat"
            elif goat5 == "NomadGoat":
                return "NomadGoat"
            elif goat5 == "ArmyGoat":
                return "ArmyGoat"
            elif goat5 == "MusicalGoat":
                return "MusicalGoat"
            elif goat5 == "BoxerGoat":
                return "BoxerGoat"

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
                return "HappyGoat"
            elif goat6 == "SadGoat":
                return "SadGoat"
            elif goat6 == "TropicalGoat":
                return "TropicalGoat"
            elif goat6 == "AnxiousGoat":
                return "AnxiousGoat"
            elif goat6 == "GamerGoat":
                return "GamerGoat"
            elif goat6 == "AngryGoat":
                return "ArmyGoat"
            elif goat6 == "HealthyGoat":
                return "HealthyGoat"
            elif goat6 == "SpiderGoat":
                return "SpiderGoat"
            elif goat6 == "NomadGoat":
                return "NomadGoat"
            elif goat6 == "ArmyGoat":
                return "ArmyGoat"
            elif goat6 == "MusicalGoat":
                return "MusicalGoat"
            elif goat6 == "BoxerGoat":
                return "BoxerGoat"
            
            
clock = pygame.time.Clock()

# <-- Start of game loop --> 
mainMenu = True
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

while(mainMenu == True):
    
    screen.fill(navy)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()
    
    if titleButton.draw() == True:
        titleButtonCounter = titleButtonCounter + 1
        screen.fill(navy)
        screen.blit(goatQuizTitleDown,(240, 64))
        screen.blit(startButtonImg,(384,570))
        pygame.display.flip()
        sleep(.1)
            
    if titleButtonCounter == 1:
        while loopOnce <= 45:
            
            screen.fill(navy)
            screen.blit(startButtonImg,(384,570))
            screen.blit(goatQuizTitle,(240, 64))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    False
                    
            goatGuySlide = goatGuySlide + 3
            screen.blit(goatGuyNormal,(goatGuySlide, 483))
            
            if goatGuySlide > -70:
                break
            
            
            clock.tick(60)
            pygame.display.flip()
            loopOnce = loopOnce + 1
        screen.blit(goatGuyNormal,(-70,483))
        goatGuy1Text = defFont.render("Hey dont press that!", True, white)
        screen.blit(goatGuy1Text,(150,483))
    elif titleButtonCounter == 2:
        screen.blit(goatGuyNormal,(-70,483))
        goatGuy2Text = defFont.render("Im warning you, dont press it!", True, white)
        screen.blit(goatGuy2Text,(150,483))
    elif titleButtonCounter == 3:
        screen.blit(goatGuyNormal,(-70,483))
        goatGuy3Text = defFont.render("You better stop that right now!", True, white)
        screen.blit(goatGuy3Text,(150,483))
    elif titleButtonCounter == 4:
        screen.blit(goatGuyAngry,(-70,483))
        goatGuy4Text = defFont.render("ENOUGH IS ENOUGH STOP RIGHT NOW!", True, white)
        screen.blit(goatGuy4Text,(150,483))
    elif titleButtonCounter == 5:
        screen.blit(goatGuyAngry,(-70,483))
        goatGuy5Text = defFont.render("ALRIGHT THAT'S.....", True, white)
        screen.blit(goatGuy5Text,(150,483))
        screen.blit(goatQuizTitle,(240, 64))
        screen.blit(startButtonImg,(384,570))
        pygame.display.flip()
        sleep(.8)
        titleButtonCounter = titleButtonCounter + 1
    elif titleButtonCounter == 6:
        screen.blit(goatGuyNormal,(-70,483))
        goatGuy6Text = defFont.render("Wait...something's wrong...", True, white)
        screen.fill(navy)
        screen.blit(goatGuyNormal,(-70,483))
        screen.blit(goatGuy6Text,(150,483))
        screen.blit(goatQuizTitle,(240, 64))
        screen.blit(startButtonImg,(384,570))
        pygame.display.flip()
        sleep(3)
        titleButtonCounter = titleButtonCounter + 1
    elif titleButtonCounter == 7:
        goatGuy7Text = defFont.render("Im really serious this time", True, white)
        screen.fill(navy)
        screen.blit(goatGuyNormal,(-70,483))
        screen.blit(goatGuy7Text,(150,483))
        screen.blit(goatQuizTitle,(240, 64))
        screen.blit(startButtonImg,(384,570))
        pygame.display.flip()
        sleep(2)
        titleButtonCounter = titleButtonCounter + 1
    elif titleButtonCounter == 8:
        goatGuy8Text = defFont.render("DO NOT PRESS THAT BUTTON AGAIN", True, white)
        screen.fill(navy)
        screen.blit(goatGuyAngry,(-70,483))
        screen.blit(goatGuy8Text,(150,483))
        screen.blit(goatQuizTitle,(240, 64))
        screen.blit(startButtonImg,(384,570))
        pygame.display.flip()
    elif titleButtonCounter == 9:
        goatGuy9Text = defFont.render("What have you done...", True, white)
        screen.fill(navy)
        screen.blit(goatGuyNormal,(-70,483))
        screen.blit(goatGuy9Text,(150,483))
        screen.blit(goatQuizTitle,(240, 64))
        screen.blit(startButtonImg,(384,570))
        pygame.display.flip()
        sleep(2)
        while True:
                
            screen.fill(navy)
            screen.blit(goatGuyShocked,(-70,483))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    False
                    
            goatQuizSlide2 = goatQuizSlide2 + 4
            screen.blit(goatQuizTitle,(240, goatQuizSlide2))
            
            if goatQuizSlide2 > 200:
                startButtonSlide2 = startButtonSlide2 + 4
                screen.blit(startButtonImg,(384, startButtonSlide2))
            else:
                screen.blit(startButtonImg,(384,570))
            
            if goatQuizSlide2 > 1050:
                break
            
            clock.tick(60)
            pygame.display.flip()
        titleButtonCounter = titleButtonCounter + 1
    elif titleButtonCounter == 10:
        goatGuy10Text = defFont.render("LOOK WHAT YOU DID! YOU BROKE IT!", True, white)
        screen.fill(navy)
        screen.blit(goatGuyAngry,(-70,483))
        screen.blit(goatGuy10Text,(150,483))
        pygame.display.flip()
        sleep(3)
        titleButtonCounter = titleButtonCounter + 1
    elif titleButtonCounter == 11:
        goatGuy11Text = defFont.render("THIS IS WHY WE CANT HAVE NICE THINGS!", True, white)
        screen.fill(navy)
        screen.blit(goatGuyAngry,(-70,483))
        screen.blit(goatGuy11Text,(140,483))
        pygame.display.flip()
        sleep(2.5)
        titleButtonCounter = titleButtonCounter + 1
    elif titleButtonCounter == 12:
        goatGuy12Text = defFont.render("Whatever your fun's over", True, white)
        screen.fill(navy)
        screen.blit(goatGuyAngry,(-70,483))
        screen.blit(goatGuy12Text,(150,483))
        pygame.display.flip()
        sleep(2)
        titleButtonCounter = titleButtonCounter + 1
    elif titleButtonCounter == 13:
        goatGuy13Text = defFont.render("You ruined my quiz, Goodbye", True, white)
        screen.fill(navy)
        screen.blit(goatGuyNormal,(-70,483))
        screen.blit(goatGuy13Text,(150,483))
        pygame.display.flip()
        sleep(3)
        pygame.quit()
    
    if titleButtonCounter < 10:
        if startButton.draw() == True:
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
    
    #Question1
    while(True):
        
        screen.fill(navy)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit()
        
        goatResponse = Questions.question("Describe your personality with a food", "Steak", "BoxerGoat", "Lucky Charms", "HappyGoat", "Pineapple", "TropicalGoat", "Coffee", "AnxiousGoat", "Hot Dogs", "SpiderGoat", "McDonalds", "ArmyGoat")
        
        if goatResponse == "HappyGoat":
            happyGoat += 1
            break
        elif goatResponse == "SadGoat":
            sadGoat += 1
            break
        elif goatResponse == "TropicalGoat":
            tropicalGoat += 1
            break
        elif goatResponse == "AnxiousGoat":
            anxiousGoat += 1
            break
        elif goatResponse == "GamerGoat":
            gamerGoat += 1
            break
        elif goatResponse == "AngryGoat":
            angryGoat += 1
            break
        elif goatResponse == "HealthyGoat":
            healthyGoat += 1
            break
        elif goatResponse == "SpiderGoat":
            spiderGoat += 1
            break
        elif goatResponse == "NomadGoat":
            nomadGoat += 1
            break
        elif goatResponse == "ArmyGoat":
            armyGoat += 1
            break
        elif goatResponse == "MusicalGoat":
            musicalGoat += 1
            break
        elif goatResponse == "BoxerGoat":
            boxerGoat += 1
            break

        clock.tick(60)
        pygame.display.flip()
    
    #Question2
    while(True):
        
        screen.fill(navy)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit()
        
        goatResponse = Questions.question("Favourite type of drink", "G-Fuel", "GamerGoat", "Pop", "HappyGoat", "Water", "HealthyGoat", "Tea", "AnxiousGoat", "Energy Drink", "BoxerGoat", "Milk", "ArmyGoat")
        
        if goatResponse == "HappyGoat":
            happyGoat += 1
            break
        elif goatResponse == "SadGoat":
            sadGoat += 1
            break
        elif goatResponse == "TropicalGoat":
            tropicalGoat += 1
            break
        elif goatResponse == "AnxiousGoat":
            anxiousGoat += 1
            break
        elif goatResponse == "GamerGoat":
            gamerGoat += 1
            break
        elif goatResponse == "AngryGoat":
            angryGoat += 1
            break
        elif goatResponse == "HealthyGoat":
            healthyGoat += 1
            break
        elif goatResponse == "SpiderGoat":
            spiderGoat += 1
            break
        elif goatResponse == "NomadGoat":
            nomadGoat += 1
            break
        elif goatResponse == "ArmyGoat":
            armyGoat += 1
            break
        elif goatResponse == "MusicalGoat":
            musicalGoat += 1
            break
        elif goatResponse == "BoxerGoat":
            boxerGoat += 1
            break

        clock.tick(60)
        pygame.display.flip()
    
    #Question3
    while(True):
        
        screen.fill(navy)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit()
        
        goatResponse = Questions.question("Favourite school subject", "Math", "HappyGoat", "Gym", "BoxerGoat", "English", "AnxiousGoat", "Lunch", "GamerGoat", "Science", "SpiderGoat", "History", "NomadGoat")
        
        if goatResponse == "HappyGoat":
            happyGoat += 1
            break
        elif goatResponse == "SadGoat":
            sadGoat += 1
            break
        elif goatResponse == "TropicalGoat":
            tropicalGoat += 1
            break
        elif goatResponse == "AnxiousGoat":
            anxiousGoat += 1
            break
        elif goatResponse == "GamerGoat":
            gamerGoat += 1
            break
        elif goatResponse == "AngryGoat":
            angryGoat += 1
            break
        elif goatResponse == "HealthyGoat":
            healthyGoat += 1
            break
        elif goatResponse == "SpiderGoat":
            spiderGoat += 1
            break
        elif goatResponse == "NomadGoat":
            nomadGoat += 1
            break
        elif goatResponse == "ArmyGoat":
            armyGoat += 1
            break
        elif goatResponse == "MusicalGoat":
            musicalGoat += 1
            break
        elif goatResponse == "BoxerGoat":
            boxerGoat += 1
            break

        clock.tick(60)
        pygame.display.flip()
    
    #Question4
    while(True):
            
        screen.fill(navy)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit()
        
        goatResponse = Questions.question("What is your state of mind?", "Crazy", "AngryGoat", "Tired", "AnxiousGoat", "Bored", "NomadGoat", "Social", "HealthyGoat", "Fear", "ArmyGoat", "Depressed", "SadGoat")
        
        if goatResponse == "HappyGoat":
            happyGoat += 1
            break
        elif goatResponse == "SadGoat":
            sadGoat += 1
            break
        elif goatResponse == "TropicalGoat":
            tropicalGoat += 1
            break
        elif goatResponse == "AnxiousGoat":
            anxiousGoat += 1
            break
        elif goatResponse == "GamerGoat":
            gamerGoat += 1
            break
        elif goatResponse == "AngryGoat":
            angryGoat += 1
            break
        elif goatResponse == "HealthyGoat":
            healthyGoat += 1
            break
        elif goatResponse == "SpiderGoat":
            spiderGoat += 1
            break
        elif goatResponse == "NomadGoat":
            nomadGoat += 1
            break
        elif goatResponse == "ArmyGoat":
            armyGoat += 1
            break
        elif goatResponse == "MusicalGoat":
            musicalGoat += 1
            break
        elif goatResponse == "BoxerGoat":
            boxerGoat += 1
            break

        clock.tick(60)
        pygame.display.flip()
        
    clock.tick(60)
    pygame.display.flip()

print("Quiz Finished")
pygame.quit()