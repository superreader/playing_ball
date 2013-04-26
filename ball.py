# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://cs.simpson.edu
 
import pygame
 
# Define some colors
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
blue     = (  50,  50, 255)
green    = (   0, 255,   0)
dkgreen  = (   0, 100,   0)
red      = ( 255,   0,   0)
purple   = (0xBF,0x0F,0xB5)
brown    = (0x55,0x33,0x00)

#ball speed contoller 
ball_speed = 2

#ball direction
ball_direction = [1,1]

# Function to draw the background
def draw_background(screen):
    # Set the screen background
    screen.fill(white)
 
def draw_bar(screen,x,y):
    #bar
    pygame.draw.rect(screen,green,[0+x,0+y,70,10],0)
     
def draw_ball(screen,x,y):
    #ball
    pygame.draw.circle(screen,red,[35+x,5+y],7,0)

def judge(screen,ball_position):
    #
    if ball_position[1] > 455 :
        screen.fill(red)
    

def move_ball(screen,ball_position):

    #x
    # out the area -> move commonly
    if not(ball_position[0] < 640 and ball_position[0] > 0):
        ball_direction[0] = ball_direction[0] * -1 
    #add ball speed
    ball_position[0] = ball_position[0] + ball_direction[0] * ball_speed
    
    #y
    # in the area -> move commonly
    if not(ball_position[1] < 460 and ball_position[1] > 0):
        ball_direction[1] = ball_direction[1] * -1 
    #add ball speed
    ball_position[1] = ball_position[1] + ball_direction[1] * ball_speed
    
    #draw ball
    draw_ball(screen,ball_position[0],ball_position[1])
    
def bump_judge(screen,ball_position,bar_position):
    if ball_position[0] < bar_position[0]+35 and ball_position[0] > bar_position[0]-35 and ball_position[1] == bar_position[1] :
    
        ball_direction[0] = ball_direction[0] * -1 
        ball_direction[1] = ball_direction[1] * -1 
        print "test"
    ball_position[0] = ball_position[0] + ball_direction[0] * ball_speed
    ball_position[1] = ball_position[1] + ball_direction[1] * ball_speed


pygame.init()
 
        
screen = pygame.display.set_mode((640, 480))
 
# Speed in pixels per frame
x_speed=0
y_speed=0
 
# Current position
x_coord=300
y_coord=450

#move vall position
ball_position = [150,450]
 
clock = pygame.time.Clock()
 
done = False
while done == False:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
             
        # User pressed down on a key
        if event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed=-5
            if event.key == pygame.K_RIGHT:
                x_speed=5
            if event.key == pygame.K_UP:
                y_speed=-5
            if event.key == pygame.K_DOWN:
                y_speed=5
                 
        # User let up on a key
        if event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT:
                x_speed=0
            if event.key == pygame.K_RIGHT:
                x_speed=0
            if event.key == pygame.K_UP:
                y_speed=0
            if event.key == pygame.K_DOWN:
                y_speed=0
 
    # Move the object according to the speed vector.
    x_coord=x_coord+x_speed
    y_coord=y_coord+y_speed
     
    draw_background(screen)
 
    # Draw the item where the mouse is.
    draw_bar(screen,x_coord,y_coord)

    bar_position = [x_coord,y_coord]

    #bar judge
    bump_judge(screen,ball_position,bar_position)
    
    #move ball
    move_ball(screen,ball_position)
    
    #judge bump
    bump_judge(screen,ball_position,bar_position)
    

    judge(screen,ball_position)
    
    pygame.display.flip()
    clock.tick(40)
     
pygame.quit ()
