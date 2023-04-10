#My fisrt python project using pygame
#This game is frame rate independent
#Animations use delta time not FPS

####################imports#################### 
import pygame, time, math, random

####################init pygame and frame timing####################
#CONSTANTS
pygame.init()
FPS = pygame.time.Clock() #called last at end of game loop   
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))  
VELOCITY_1 = 100
#VARIABLES
seconds = 0
minutes = 0
prev_time = time.time() # critical for init of timing mehcanics line 40

#Global variables
done = False
x = 0
y = 0
EPOCH_TIMESTAMP = int(time.time())
BLACK =     (0,0,0) #tuples are used to store multiple items in a single variable
WHITE =     (225,225,225) #RGB VALUES red green blue
RED =       (225,0,0)
GREEN =     (0, 225, 0)
BLUE =      (0, 0, 225)
GROUND =    (600)
text_font = pygame.font.SysFont("Adrial", 20)

#Helper function to render text to screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    DISPLAYSURF.blit(img, (x, y)) #blit text image to said display surface

#Experimental unit circle functions
def draw_unit_circle_1():
    pygame.draw.arc(DISPLAYSURF, RED, (700,40,20,20), 0, 2 * (math.pi)) #Rect(left, top, width, height)

def draw_unit_circle_2():
    pygame.draw.circle(DISPLAYSURF, GREEN, (750,50), 10, width=1) # a radius of 1 is literaly 1 pixel # width = hollow

class RandomCircles():
    def __init__(
            self,
            thisX = 390,
            thisY = 390
        ): #think of this as a constructor u r used to in other languages 
        super().__init__()
        self.thisX = thisX
        self.thisY = thisY

    def movement(self):
        if self.thisY < GROUND - 10:
            self.thisY += VELOCITY_1 * dt 

    def draw(self):
        self.draw_this_cirles_angle = pygame.draw.line(DISPLAYSURF, GREEN, (self.thisX, self.thisY), (self.thisX + 9, self.thisY))
        self.draw_unit_circle = pygame.draw.circle(DISPLAYSURF, RED, (self.thisX,self.thisY), 10, width = 1)
        self.movement()


####################Instantiate Objects####################
C1 = RandomCircles(390,390)

####################Game Loop####################
while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  #end point
            done = True

    ####################Within Game Loop Timing Mechanics####################
    current_frame_rate = FPS.get_fps()
    epoch = int(time.time())
    if EPOCH_TIMESTAMP != epoch: #this allows for exact second count
        seconds = seconds + 1
        if seconds == 60:
            seconds = 0
            minutes = minutes + 1
        EPOCH_TIMESTAMP = epoch
    #compute delta time, previous time will be different that now time
    #on every cycle of while loop
    now = time.time()       #float
    dt = now - prev_time    #float # "dt" can be used for adjusting movements
                            #ie: object_position += velocity * dt
    prev_time = now         #float

    ####################Clear Screen####################
    DISPLAYSURF.fill(BLACK)
    
    ####################Timing Display####################
    draw_text("MINUTES:",text_font, GREEN, 10, 10)
    draw_text("SECONDS:",text_font, GREEN, 10, 25)
    draw_text("FPS: ",text_font, GREEN, 10, 40)
    convertedMINUTES = str(minutes)
    convertedEPOCH = str(seconds)
    convertedFPS = str(int(current_frame_rate))
    draw_text(convertedMINUTES,text_font, GREEN, 80, 10)
    draw_text(convertedEPOCH,text_font, GREEN, 85, 25)
    draw_text(convertedFPS,text_font, GREEN, 45, 40)

    ####################Game Logic####################
    if x < SCREEN_WIDTH - 10:
        x += VELOCITY_1 * dt

    ####################Draw Logic####################
    #Draw test rect    
    pygame.draw.rect(DISPLAYSURF, RED, pygame.Rect(x,y,10,10))            
    
    #Draw static unit circles
    draw_unit_circle_1()
    draw_unit_circle_2()

    #Draw dynamic unit circles
    C1.draw()
    


    ####################REFRESH LOGIC####################
    #redraws entire DISPLAYSURF, but does not clear DISPLAYSURF
    pygame.display.flip()
    #Re-iterates frame per second / doing this outside the loop does not change fps
    FPS.tick(60)