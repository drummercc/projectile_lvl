import pygame, sys
import math
import random

def ball_animation():
    global ball_speed_x, ball_speed_y, ball_angle, lives, i
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.bottom >= screen_height* 78/80:
        ball_speed_x = 0
        ball_speed_y = 0
        ball.bottom = screen_height / 80 * 64
        ball.left = screen_width / 120 * 30.4
        lives -= 1
    if ball.colliderect(line):
        ball_speed_y = 0
    if ball.colliderect(target_rect):
        ball_speed_x = 0
        ball_speed_y = 0
        completed()
    if ball.colliderect(wall):
        ball_speed_x = 0
        ball_speed_y = 0
        ball.bottom = screen_height / 80 * 64
        ball.left = screen_width / 120 * 30.4
        lives -= 1

    #if ball.top <= -15:
    #    ball_speed_x = 0
    #    ball_speed_y = 0
    #    ball.bottom = 650
    #    ball.left = 304
    #    lives -= 1

    if ball.right >= screen_width + 20:
        ball_speed_x = 0
        ball_speed_y = 0
        ball.bottom = screen_height / 80 * 64
        ball.left = screen_width / 120 * 30.4
        lives -= 1

def update():
    global ball_velocity, ball_angle, lives, i
    if lives == 0:
        i = random.randrange(27, 36, 1)
        lives = 3
    if ball_velocity <= 7:
        ball_velocity = 7
    if ball_velocity > 20:
        ball_velocity = 20
    if ball_velocity <= 20:
        ball_velocity += ball_velocity_increment
    if ball_angle < -80:
        ball_angle = -80
    if ball_angle > 0:
        ball_angle = 0
    if ball_angle >= -80:
        ball_angle += ball_angle_increment


def completed():
    global background
    background = pygame.image.load('ChallengeRoom1(Door1Open).jpg')

# General Set up
pygame.init()
clock = pygame.time.Clock()

#Setting up main window

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('projectile')
i = 35

#Graphics
target = pygame.image.load('Target(1).png')
target_rect = pygame.Rect(screen_width * i/48, screen_height * 70/72, target.get_width() - 2, 1)

wall = pygame.Rect(screen_width / 120 * 60, screen_height * 66/100, screen_width / 120 * 5, screen_height * 34/100)
ball = pygame.Rect(screen_width / 120 * 30.4,screen_height / 80 * 64,15 ,15)
line = pygame.Rect(screen_width / 120 * 28,screen_height / 80 * 65,50, 3)

gravity = 9.8

ball_speed_x = 0
ball_speed_y = 0
ball_angle_increment = 0
ball_angle = 0
ball_velocity_increment = 0
ball_velocity = 7
gravity = 9.8
lives = 3


launcher = pygame.image.load('Projectile-Launcher.png')
background = pygame.image.load('ChallengeRoom1.jpg')

player = pygame.image


bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

font = pygame.font.SysFont("comicsans", 30, True)


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



# Key Actions
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                ball_angle_increment += 0.2
            if event.key == pygame.K_UP:
                ball_angle_increment -= 0.2
            if event.key == pygame.K_LEFT:
                ball_velocity_increment -= 0.1
            if event.key == pygame.K_RIGHT:
                ball_velocity_increment += 0.1
            if event.key == pygame.K_RETURN:
                if ball_speed_x == 0 or ball_speed_y == 0:
                    ball_speed_x = ball_velocity * math.cos(ball_angle * math.pi/180)
                    ball_speed_y = ball_velocity * math.sin(ball_angle * math.pi/180)
                else:
                    j = 5
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                ball_angle_increment = 0
            if event.key == pygame.K_UP:
                ball_angle_increment = 0
            if event.key == pygame.K_LEFT:
                ball_velocity_increment = 0
            if event.key == pygame.K_RIGHT:
                ball_velocity_increment = 0
       

    
    ball_animation()
    update()
    #ball_velocity += ball_velocity_increment
    #ball_angle += ball_angle_increment
    ball_speed_y += gravity/60  
    
    #Visuals
    screen.fill(bg_color)
    screen.blit(background, (0,0))
    screen.blit(target, (screen_width * i/48, screen_height * 36/40))
    target_rect = pygame.Rect(screen_width * i/48, screen_height * 69/72, target.get_width(), 2)
    pygame.draw.ellipse(screen, (0,200,200), ball)
    pygame.draw.rect(screen, (0,0,0), line)
    text = font.render("Angle " + str(-1 * ball_angle), 30, (200,0,0))
    text1 = font.render("Velocity " + str(ball_velocity), 30, (200,0,0))
    textlives = font.render("Lives Left: " + str(lives), 30, (200,0,0))
    screen.blit(textlives, (screen_width * 6/8, screen_height * 1/12))
    screen.blit(text1, (screen_width/6, screen_height/8))
    screen.blit(text, (screen_width/6, screen_height/12))
    #Launcher Animation
    launcher_copy = pygame.transform.rotate(launcher, -1 * ball_angle)
    screen.blit(launcher_copy, (screen_width / 120 * 27 - int(launcher_copy.get_width() / 4), screen_height / 120 * 95 - int(launcher_copy.get_height() /2)))
    

    pygame.display.flip()
    clock.tick(60)

