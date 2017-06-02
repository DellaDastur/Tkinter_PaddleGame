import pygame, sys
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode([640,480])
black = [0, 0, 0]
myfont = pygame.font.SysFont('Arial', 15)

#the game's variables
highscorecount = 0
scorecount = 0
ball_x = 200
ball_y = 200
ball_radius = 10
ball_color = [222,50,50]
ball_speed_y = 3
ball_speed_x = 3

running = True
#game loop
while running:
    for event in pygame.event.get():
        #check if you've exited the game
        if event.type == pygame.QUIT:
            running = False
    
    #pause for 20 milliseconds
    pygame.time.delay(20)
    #make the screen completely white
    screen.fill(black)
    ball_rect = pygame.Rect(ball_x-ball_radius, ball_y-ball_radius, ball_radius*2,ball_radius*2)
    
    pygame.draw.circle(screen, ball_color, [ball_x, ball_y], ball_radius, 0)
    
    pygame.display.update()


pygame.quit()
