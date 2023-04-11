# My first python program ever
# Game is frame rate independent
# Animations use delta time not FPS

####################imports#################### 
import pygame, time, math, random

####################init pygame and frame timing####################
#Game mechanic constants
pygame.init()
FPS = pygame.time.Clock() #called last at end of game loop   
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))  

#Timing variables
seconds = 0
minutes = 0
prev_time = time.time() # critical for init of timing mehcanics line 40

#Physics variables
VELOCITY_1 =    100     # traverses 800px in about 8.5 seconds # is striclty a speed
VELOCITY_2 =    10      # first delta time iteration
GROUND =        (600)   # bottom of the screen
GRAVITY =       100     # traverses 800px in about 8.5 seconds
DELTA_TIME =    float

#"ACCELERATION" is a special case variable that involves some math"
ACCELERATION = 1         
    # to be used with gravity # is a measure of the speed and direction of motion
    # eg: ACCELERATION = DELTATIME * VELOCITY / TIME
    # TIME could = the milliseconds the object is not at rest on ground level

#Other Global variables
done = False                        # is game seq complete
x = 0
y = 0
EPOCH_TIMESTAMP = int(time.time())
BLACK =     (0,0,0)                 #tuples are used to store multiple items in a single variable
WHITE =     (225,225,225)           #RGB VALUES red green blue
RED =       (225,0,0)
GREEN =     (0, 225, 0)
BLUE =      (0, 0, 225)
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

####################Circle Class####################
class RandomCircles():
    def __init__( #think of this as a constructor u r used to in other languages
            self,
            thisX = 390,
            thisY = 390,
            thisAngleInteger = 1,
            thisAngle = 0 / 180 * math.pi,
            thisDT = DELTA_TIME,
            thisDegree = .017 # found this to be the smoothest measure of degree ticks for a unit circle
        ):  
        super().__init__()
        self.thisX = thisX
        self.thisY = thisY
        self.thisAngleInteger = thisAngleInteger
        self.thisAngle = thisAngle
        self.thisDT = thisDT
        self.thisDegree = thisDegree

    def movement(self):
        self.thisX += math.cos(self.thisAngle) * (VELOCITY_2 * DELTA_TIME) 
        self.thisY -= math.sin(self.thisAngle) * (VELOCITY_2 * DELTA_TIME)
        self.thisAngleInteger += 1
        self.thisAngle = self.thisAngleInteger / 180 * math.pi

    def draw(self):
        # this draw a line/ ray point to the angle at which the circle is traveling
        self.draw_this_cirles_angle = pygame.draw.line(
            DISPLAYSURF,
            WHITE, 
            (self.thisX, self.thisY), 
            (self.thisX + 10 * math.cos(self.thisAngle), self.thisY - 10 * math.sin(self.thisAngle))
        )
        self.draw_unit_circle = pygame.draw.circle(DISPLAYSURF, RED, (self.thisX,self.thisY), 10, width = 1)
        self.movement()

####################Instantiate Objects####################
C1 = RandomCircles()

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
    DELTA_TIME = dt         #ie: object_position += velocity * dt # this makes dt GLOBAL
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
    #move rect
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