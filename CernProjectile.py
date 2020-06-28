import pygame, sys
import math
import random

def ball_animation():
    global ball_speed_x, ball_speed_y, ball_angle, lives, i, Background_game, player_x, background
    screen.fill(bg_color)
    screen.blit(background_game, (0,0))
    screen.blit(target, (screen_width * i/48, screen_height * 36/40))
    screen.blit(astronaut, (screen_width * 4/6, screen_height / 60 *39))
    target_rect = pygame.Rect(screen_width * i/48, screen_height * 69/72, target.get_width(), 2)
    pygame.draw.ellipse(screen, (0,200,200), ball)
    pygame.draw.rect(screen, (0,0,0), line)
    launcher_copy = pygame.transform.rotate(launcher, -1 * ball_angle)
    screen.blit(launcher_copy, (screen_width / 120 * 27 - int(launcher_copy.get_width() / 4), screen_height / 120 * 95 - int(launcher_copy.get_height() /2)))
    text = font.render("Angle " + "{:.2f}".format(-1 * ball_angle), 30, (200,0,0))
    text1 = font.render("Velocity " + "{:.2f}".format(ball_velocity), 30, (200,0,0))
    textlives = font.render("Lives Left: " + str(lives), 30, (200,0,0))
    screen.blit(textlives, (screen_width * 6/8, screen_height * 1/12))
    screen.blit(text1, (screen_width/6, screen_height/8))
    screen.blit(text, (screen_width/6, screen_height/12))
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
        while player_x < 700:
            background = pygame.image.load('ChallengeRoom1(Door1Open).jpg')
            completed()
    if ball.colliderect(wall):
        ball_speed_x = 0
        ball_speed_y = 0
        ball.bottom = screen_height / 80 * 64
        ball.left = screen_width / 120 * 30.4
        lives -= 1


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
    global background, player_x, walkcount
    if walkcount + 1 >= 27:
        walkcount = 0
    screen.blit(background, (0,0))
    screen.blit(launcher, (screen_width / 120 * 27 - int(launcher.get_width() / 4), screen_height / 120 * 95 - int(launcher.get_height() /2)))
    screen.blit(background, (0,0))
    screen.blit(launcher, (screen_width / 120 * 27 - int(launcher.get_width() / 4), screen_height / 120 * 95 - int(launcher.get_height() /2)))
    screen.blit(target, (screen_width * i/48, screen_height * 36/40))
    screen.blit(text_launcher, (screen_width *2 / 6, screen_height/8))
    screen.blit(astronaut, (screen_width * 4/6, screen_height / 60 *39))
    screen.blit(player_walking [walkcount//7], (player_x, player_y))
    screen.blit(door_frame, (screen_width * 46 / 100, screen_height * 66 / 100))
    player_x += 1.5
    walkcount += 1
    pygame.display.update()


    

def player_animation():
    global walkcount, player_x, i, font, text_launcher, walking, sound1, sound2, j, speech
    screen.blit(background, (0,0))
    screen.blit(launcher, (screen_width / 120 * 27 - int(launcher.get_width() / 4), screen_height / 120 * 95 - int(launcher.get_height() /2)))
    screen.blit(target, (screen_width * i/48, screen_height * 36/40))
    screen.blit(text_launcher, (screen_width *2 / 6, screen_height/8))
    screen.blit(astronaut, (screen_width * 4/6, screen_height / 60 *39))
    if walkcount + 1 >= 27:
        walkcount = 0
    if player_x < 0:
        player_x = 0
    if walking:
        screen.blit(player_walking [walkcount//7], (player_x, player_y))
        walkcount += 1
    if walking == False:
        screen.blit(player_standing, (player_x, player_y))
    if player_x > screen_width / 100 * 41:
        player_x = screen_width / 100 * 41
        if j == 1:
            speech = speech_1
            screen.blit(speech, (screen_width * 3/8, screen_height * 3/8))
            pygame.display.flip()
            sound1.play()
            pygame.time.delay(12000)
            sound2.play()
            pygame.time.delay(14000)
            fill()
            screen.blit(speech_2, (screen_width * 3/8, screen_height * 3/8))
            pygame.display.flip()
            sound3.play()
            pygame.time.delay(3000)
            fill()
            screen.blit(speech_3, (screen_width * 3/8, screen_height * 3/8))
            pygame.display.flip()
            pygame.time.delay(3000)
            fill()
            screen.blit(speech_4, (screen_width * 3/8, screen_height * 3/8))
            pygame.display.flip()
            fill()
            pygame.time.delay(3000)
            screen.blit(speech_5, (screen_width * 3/8, screen_height * 3/8))
            pygame.display.flip()
            pygame.time.delay(3800)
            fill()
            screen.blit(speech_6, (screen_width * 3/8, screen_height * 3/8))
            pygame.display.flip()
            pygame.time.delay(3000)
            fill()
            text_launcher = font.render("Press Enter At Launcher", 40, (200,0,0))
            j = 0
    if j == 0:
       if player_x < screen_width / 100 * 25 and player_x > screen_width / 100:
            border = pygame.Rect(screen_width / 100 * 15, screen_height / 100 * 66, 215, 26)
            pygame.draw.rect(screen, (0,0,0), border)
            text_enter = font.render("[Press Enter Here]",  30, (255,255,255))
            screen.blit(text_enter, (screen_width / 100 * 15, screen_height / 100 * 66))
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_RETURN:
                        intro = False
                        playing = True
        
    pygame.display.update()

def fill():
    global player_x
    screen.blit(background, (0,0))
    screen.blit(launcher, (screen_width / 120 * 27 - int(launcher.get_width() / 4), screen_height / 120 * 95 - int(launcher.get_height() /2)))
    screen.blit(target, (screen_width * i/48, screen_height * 36/40))
    screen.blit(text_launcher, (screen_width *2 / 6, screen_height/8))
    screen.blit(astronaut, (screen_width * 4/6, screen_height / 60 *39))
    screen.blit(player_standing, (player_x, player_y))




# General Set up
pygame.init()
clock = pygame.time.Clock()

#Setting up main window

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('projectile')
i = 35
j = 1

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
background_game = pygame.image.load('ChallengeRoom1(game scene).jpg')
door_frame = pygame.image.load('DoorFrame.png')
astronaut = pygame.image.load('astronaut instructor.png')

speech_1 = pygame.image.load("IntroText(1).png")
speech_2 = pygame.image.load("IntroText(2).png")
speech_3 = pygame.image.load("IntroText(3).png")
speech_4 = pygame.image.load("IntroText(4).png")
speech_5 = pygame.image.load("IntroText(5).png")
speech_6 = pygame.image.load("IntroText(6).png")

sound1 = pygame.mixer.Sound('Part-1.wav')
sound2 = pygame.mixer.Sound('Part-2.wav')
sound3 = pygame.mixer.Sound('Part-3.wav')
sound4 = pygame.mixer.Sound('Part-4_1.wav')
sound5 = pygame.mixer.Sound('Part-5_1.wav')


player_walking = [pygame.image.load('charv2(1).png'), pygame.image.load('charv2(2).png'), pygame.image.load('charv2(3).png'), pygame.image.load('charv2(4).png')]
player_standing = pygame.image.load('charv2(5).png')
player_width = 110
player_height = 160
player_vel = 5
walkcount = 0
player_x = 0
player_y = screen_height / 60 *43
walking = False

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

font = pygame.font.SysFont("comicsans", 30, True)
text_launcher = font.render("", 40, (200,0,0))

#Stages
intro = True
playing = False


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    while intro:

            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x -= 1.5
                    walking = True
                if event.key == pygame.K_RIGHT:
                    player_x += 1.5
                    walking = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    walking = False
                if event.key == pygame.K_RIGHT:
                    walking = False
                if event.key == pygame.K_RETURN:
                    if player_x < screen_width / 100 * 25 and player_x > screen_width / 100 * 18:
                        intro = False
                        playing = True
                        break

           
            player_animation()
            clock.tick(60)


# Key Actions
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
            ball_angle_increment += 0.02 
        if event.key == pygame.K_UP:
            ball_angle_increment -= 0.02
        if event.key == pygame.K_LEFT:
            ball_velocity_increment -= 0.01
        if event.key == pygame.K_RIGHT:
            ball_velocity_increment += 0.01
        if event.key == pygame.K_RETURN:
            if ball_speed_x == 0 or ball_speed_y == 0:
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
    ball_speed_y += gravity/60  


    #Launcher Animation
    #launcher_copy = pygame.transform.rotate(launcher, -1 * ball_angle)
    #screen.blit(launcher_copy, (screen_width / 120 * 27 - int(launcher_copy.get_width() / 4), screen_height / 120 * 95 - int(launcher_copy.get_height() /2)))
    
     

    
    ball_animation()
    update()
    #ball_velocity += ball_velocity_increment
    ball_speed_y += gravity/60  
    
    
    #Visuals
    
    #screen.fill(bg_color)
    #screen.blit(background, (0,0))
    #screen.blit(target, (screen_width * i/48, screen_height * 36/40))
    #target_rect = pygame.Rect(screen_width * i/48, screen_height * 69/72, target.get_width(), 2)
    #pygame.draw.ellipse(screen, (0,200,200), ball)
    #pygame.draw.rect(screen, (0,0,0), line)
    #text = font.render("Angle " + str(-1 * ball_angle), 30, (200,0,0))
    #text1 = font.render("Velocity " + str(ball_velocity), 30, (200,0,0))
    #textlives = font.render("Lives Left: " + str(lives), 30, (200,0,0))
    #screen.blit(textlives, (screen_width * 6/8, screen_height * 1/12))
    #screen.blit(text1, (screen_width/6, screen_height/8))
    #screen.blit(text, (screen_width/6, screen_height/12))
    #Launcher Animation
    #launcher_copy = pygame.transform.rotate(launcher, -1 * ball_angle)
    #screen.blit(launcher_copy, (screen_width / 120 * 27 - int(launcher_copy.get_width() / 4), screen_height / 120 * 95 - int(launcher_copy.get_height() /2)))
    

    pygame.display.flip()
    clock.tick(30)

