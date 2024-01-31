import pygame
#changed colors
PINK = (0, 0, 0)

class Paddle(pygame.sprite.Sprite):
    #this class represents a paddle. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        #call the parent class (sprite) constructor
        super().__init__()

        #Pass in the color of the paddle, its width and height,
        #set the background color and set t to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(PINK)
        self.image.set_colorkey(PINK)

        #Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        #Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        #check not going off screen
        if self.rect.y < 0:
            self.rect.y = 0

    def moveDown(self, pixels):
        self.rect.y += pixels
    #check not going too far down
        if self.rect.y > 400:
            self.rect.y = 400

