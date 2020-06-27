import pygame, sys
import math

def ball_animation():
    global ball_speed_x, ball_speed_y, ball_angle
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.bottom >= screen_height + 1:
        ball_speed_x = 0
        ball_speed_y = 0
    if ball.colliderect(line):
        ball_speed_x = 0
        ball_speed_y = 0

    if ball.top <= -15:
        ball_speed_x = 0
        ball_speed_y = 0
        ball.bottom = 650
        ball.left = 304

    if ball.right >= screen_width + 20:
        ball_speed_x = 0
        ball_speed_y = 0
        ball.bottom = 650
        ball.left = 304

def update():
    global ball_velocity, ball_angle
    if ball_velocity > 20:
        ball_velocity = 20
    if ball_velocity <= 20:
        ball_velocity += ball_velocity_increment
    if ball_angle < -90:
        ball_angle = -90
    if ball_angle >= -90:
        ball_angle += ball_angle_increment


# General Set up
pygame.init()
clock = pygame.time.Clock()

#Setting up main window
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('projectile')

ball = pygame.Rect(304,640,20 ,20)
line = pygame.Rect(280,650,50, 3)
gravity = 9.8

ball_speed_x = 0
ball_speed_y = 0
ball_angle_increment = 0
ball_angle = 0
ball_velocity_increment = 0
ball_velocity = 1
gravity = 9.8

#Graphics
launcher = pygame.image.load('Projectile Launcher.png')
#launcher.set_colorkey((0,0,0))
background = pygame.image.load('ChallengeRoom1.jpg')
#launcher.set_alpha(100)

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
                ball_speed_x = ball_velocity * math.cos(ball_angle * math.pi/180)
                ball_speed_y = ball_velocity * math.sin(ball_angle * math.pi/180)
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
    #line_animation()

    #Visuals
    screen.fill(bg_color)
    screen.blit(background, (0,0))
    pygame.draw.ellipse(screen, (10,200,200), ball)
    pygame.draw.rect(screen, (0,0,0), line)
    text = font.render("Angle " + str(-1 * ball_angle), 30, (200,0,0))
    text1 = font.render("Velocity " + str(ball_velocity), 30, (200,0,0))
    screen.blit(text1, (300, 100))
    screen.blit(text, (300, 50))
    #Launcher Animation
    launcher_copy = pygame.transform.rotate(launcher, -1 * ball_angle)
    screen.blit(launcher_copy, (270 - int(launcher_copy.get_width() / 4), 650 - int(launcher_copy.get_height() /2)))

    pygame.display.flip()
    clock.tick(60)

