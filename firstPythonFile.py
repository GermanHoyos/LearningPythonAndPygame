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
GRAVITY =       0.5     # traverses 800px in about 8.5 seconds
BOUNCE_STOP =   0.3       # This prevents infinite tiny bounces
DELTA_TIME =    float

#Other Global variables
done = False                        # is game seq complete
x = 0
y = 0
dx = 1
dy = 1
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

#Experimental unit circle functions using "arc" and "circle"
def draw_unit_circle_1():
    pygame.draw.arc(DISPLAYSURF, RED, (700,40,20,20), 0, 2 * (math.pi)) #Rect(left, top, width, height)
def draw_unit_circle_2():
    pygame.draw.circle(DISPLAYSURF, GREEN, (750,50), 10, width=1) # a radius of 1 is literaly 1 pixel # width = hollow

####################Asteroid Player1 Circle Class####################
class AsteroidPlayer(): # Use this circle for asteroids like movement
    def __init__( #think of this as a constructor u r used to in other languages
            self,
            thisX = 700,
            thisY = 60,
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
        self.draw_unit_circle = pygame.draw.circle(DISPLAYSURF, RED, (self.thisX, self.thisY), 10, width = 1)
        self.movement()

####################Stationary Unit Circle Shows cos sin tan####################
class UnitCircle():
    def __init__(self, myX = 570, myY = 50, angle = 0 / 180 * math.pi, rotation = 0):
        self.myX = myX
        self.myY = myY
        self.myAngle = angle
        self.rotation = rotation

    def draw(self):
        if self.rotation < 360:
            self.rotation += 1
            if self.rotation >= 360:
                self.rotation = 0
        self.myAngle = self.rotation / 180 * math.pi
        self.draw_unit_circle = pygame.draw.circle(DISPLAYSURF, RED, (self.myX, self.myY), 50, width = 1)
        self.draw_angle = pygame.draw.line(DISPLAYSURF, WHITE, (self.myX, self.myY), #<----------------------------ANGLE
            (self.myX + 49 * math.cos(self.myAngle), self.myY - 49 * math.sin(self.myAngle)))
        self.draw_sin = pygame.draw.line(DISPLAYSURF, WHITE, (self.myX + 49 * math.cos(self.myAngle), self.myY),#<-SIN
            (self.myX + 49 * math.cos(self.myAngle), self.myY - 49 * math.sin(self.myAngle)))        
        self.draw_cos = pygame.draw.line(DISPLAYSURF, WHITE, (self.myX, self.myY),#<-------------------------------COS
            (self.myX + 49 * math.cos(self.myAngle), self.myY))         

####################Bouncing Ball Class####################
####################Following Tutorial####################
####################https://www.youtube.com/watch?v=5j0uU3aJxJM&t=1204s####################
####################Current Time Stamp 27:04####################
class Ball:
    def __init__(self, myX, myY, radius, color, mass, retention, ySpeed, xSpeed, id):
        self.myX = myX
        self.myY = myY
        self.radius = radius
        self.color = color
        self.mass = mass
        self.retention = retention
        self.ySpeed = ySpeed
        self.xSpeed = xSpeed
        self.id = id
        self.circle = ''
    
    def draw(self):
        self.circle = pygame.draw.circle(DISPLAYSURF, RED, (self.myX, self.myY), self.radius)
        self.ySpeed = self.check_gravity()
        self.update_pos()

    def check_gravity(self):
        if self.myY < 600 - self.radius:
            self.ySpeed += GRAVITY # gradualy increases over time
        else:
            if self.ySpeed > BOUNCE_STOP: # if my y speed is great enough where I want to contiue bouncing
                self.ySpeed = self.ySpeed * -1 * self.retention # flip direction and lose energy # UPWARD ^
            else:
                if abs(self.ySpeed) <= BOUNCE_STOP:
                    self.ySpeed = 0 # this prevents this.ySpeed being less than bounce stop so much its negative
                    # which would allow the previous if statement to be true
        return self.ySpeed
    
    def update_pos(self):
        self.myY += self.ySpeed
        self.myX += self.xSpeed

####################Instantiate Objects Outside Of Game loop####################
C1 = AsteroidPlayer()
C2 = UnitCircle()

ball1 = Ball(50, 50, 30, 'RED', 100, .9, 0, 0, 1)

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
    
    ####################Timing Display Logic####################
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
    #Bounce Rect
    if (x + 10 > 800 or x < 0 ):
        dx = -dx  
    x += VELOCITY_1 * dt * dx     


    ####################Draw Logic####################
    #Draw test rect    
    pygame.draw.rect(DISPLAYSURF, RED, pygame.Rect(x,y,10,10))            
    
    #Draw static unit circles
    draw_unit_circle_1()
    draw_unit_circle_2()

    #Draw dynamic unit circles
    C1.draw()
    C2.draw()

    #Draw ball experiment
    ball1.draw()
    # ball1.update_pos()
    # ball1.ySpeed = ball1.check_gravity();

    ####################REFRESH LOGIC####################
    #redraws entire DISPLAYSURF, but does not clear DISPLAYSURF
    pygame.display.flip()
    #Re-iterates frame per second / doing this outside the loop does not change fps
    FPS.tick(60)