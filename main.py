#import pygame
import pygame
pygame.init()

#import paddle class
from paddle import Paddle

#import ball class
from ball import Ball

#define colors, changed them
PINK = (252, 204, 228)
HOT_PINK = (240, 36, 135)

#create and open game window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(HOT_PINK, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(HOT_PINK, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(HOT_PINK, 20, 20)
ball.rect.x = 345
ball.rect.y = 195



#list that contains all sprites intended for use in the game
all_sprites_list = pygame.sprite.Group()

#Add the paddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

#var for game loop to continue until user exits game (pressing close button)
stillPlaying = True

#clock used to control how fast screen updates
clock = pygame.time.Clock()

#initialize player scores
scoreA = 0
scoreB = 0

#---------Main Program Loop----------
while stillPlaying:
    #---main even loop
    for event in pygame.event.get(): #user did something
        if event.type == pygame.QUIT: #if user clicked close
            stillPlaying = False #done so now we exit loop
        elif event.type==pygame.KEYDOWN:
            if event.type==pygame.K_x: #pressing the x key will quit the game
                stillPlaying = False

    #Moving the paddles when the user uses the arrow keys (player A - "W/S" keys) &  (player B - arrow keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.moveUp(5)
    if keys[pygame.K_s]:
        paddleA.moveDown(5)
    if keys[pygame.K_UP]:
        paddleB.moveUp(5)
    if keys[pygame.K_DOWN]:
        paddleB.moveDown(5)

    #---game logic
    all_sprites_list.update()

    #check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x >=690:
        ball.velocity[0]= -ball.velocity[0]
        scoreA+=1
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
        scoreB+=1
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    #detect collisions between the ball and the paddles
    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

        #---drawing code
    #First clear screen to black
    screen.fill(PINK)
    #draw the net
    pygame.draw.line(screen, HOT_PINK, [349, 0], [349, 500], 5)

    #draw all sprites
    all_sprites_list.draw(screen)

    #display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, HOT_PINK)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, HOT_PINK)
    screen.blit(text, (420, 10))

    #---update the screen with what's drawn
    pygame.display.flip()

    #---limit to 60 frames per second
    clock.tick(60)

#stops game engine once main program loop is exited
pygame.quit()