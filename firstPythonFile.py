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
BOUNCE_STOP =   0.3     # This prevents infinite tiny bounces
ROLL_STOP =     0.02
DELTA_TIME =    float

#Experimental physics variables
MINIMUM_SPEED = 0.3     # same as BOUNCE_STOP, this is used to determine when to set movement to 0 on any axis
FRICTION      = 0.05     
# track positions of mouse to get movement vector
mouse_trajectory = []

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

#function for calculating vectors
def calc_motion_vector():
    x_speed = 0
    y_speed = 0
    if len(mouse_trajectory) > 10: # mouse trajectory is a list of coords = mouse_trajectory[x][y]. the first position = [0][0] and the last position [-1][0]
        x_speed = (mouse_trajectory[-1][0] - mouse_trajectory[0][0]) / len(mouse_trajectory) # [X][y]
        y_speed = (mouse_trajectory[-1][1] - mouse_trajectory[0][1]) / len(mouse_trajectory) # [x][Y]
    return x_speed, y_speed


#Helper function to render text to screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    DISPLAYSURF.blit(img, (x, y)) #blit text image to said display surface # lit = block tansfer - draw surface on another surface

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
        self.retention = retention      # this precentage by which ySpeed is retained upon direction change
        self.ySpeed = ySpeed
        self.xSpeed = xSpeed
        self.id = id
        self.circle = ''
        self.selected = False

    
    def draw(self, mouse):
        self.circle = pygame.draw.circle(DISPLAYSURF, self.color, (self.myX, self.myY), self.radius)
        self.ySpeed = self.check_gravity()
        self.update_pos(mouse)

    def check_gravity(self):
        if not self.selected:
            if self.myY < 600 - self.radius:
                self.ySpeed += GRAVITY                              # gradualy increases yspeed over time by adding gravity to it continuesly
            else:
                if self.ySpeed > BOUNCE_STOP:                       # if self.ySpeed is great enough where I want to contiue bouncing / changing direction
                    self.ySpeed = self.ySpeed * -1 * self.retention # flip direction and lose energy # UPWARD ^
                else:
                    if abs(self.ySpeed) <= BOUNCE_STOP:
                        self.ySpeed = 0                             # if the (-) or (+) ySpeed is LESSTHAN BOUNCE_STOP, then stop bouncing # this catches the negative side of the bounce, as opposed to the positive side which # is caught by the if statement above this one
            if (self.myX < self.radius + (0) and self.xSpeed < 0) or \
                (self.myX > 800 - self.radius and self.xSpeed> 0):
                self.xSpeed *= -1 * self.retention
                if abs(self.xSpeed) < BOUNCE_STOP:
                    self.xSpeed = 0
            if self.ySpeed == 0 and self.xSpeed != 0:
                if self.xSpeed > 0:
                    self.xSpeed -= FRICTION
                    if self.xSpeed < ROLL_STOP:
                        self.xSpeed = 0
                elif self.xSpeed < 0:
                    self.xSpeed += FRICTION
                    if abs(self.xSpeed) <= ROLL_STOP:
                        self.xSpeed = 0

        else: # if ball is grabed and let go, let the downward speeds be reset such that gravity can begin acting on it again
            # self.xSpeed = 0
            # self.ySpeed = 0
            self.xSpeed = x_push
            self.ySpeed = y_push
        return self.ySpeed
    
    def update_pos(self, mouse):
        if not self.selected:
            self.myY += self.ySpeed
            self.myX += self.xSpeed
        else:
            self.myX = mouse[0]
            self.myY = mouse[1]


    def check_select(self, pos):
        self.selected = False
        if self.circle.collidepoint(pos):
            self.selected = True
        return self.selected







####################Instantiate Objects Outside Of Game loop####################
C1 = AsteroidPlayer()
C2 = UnitCircle()

ball1 = Ball(50, 50, 30, 'GREEN', 100, .9, 0, 0, 1)

####################Game Loop####################
while not done:

    mouse_coords = pygame.mouse.get_pos()
    mouse_trajectory.append(mouse_coords)
    if len(mouse_trajectory) > 20:
        mouse_trajectory.pop(0) # first in first out
    x_push, y_push = calc_motion_vector()

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  #end point
            done = True

        #detect mouse events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # 1 = left mouse click
                if ball1.check_select(event.pos):
                    active_select = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_select = False
                ball1.check_select((-1111,-1111))

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
    ball1.draw(mouse_coords)
    # ball1.update_pos()
    # ball1.ySpeed = ball1.check_gravity();

    ####################REFRESH LOGIC####################
    #redraws entire DISPLAYSURF, but does not clear DISPLAYSURF
    pygame.display.flip()
    #Re-iterates frame per second / doing this outside the loop does not change fps
    FPS.tick(60)