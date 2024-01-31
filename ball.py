import pygame
from random import randint

#changed colors
PINK = (0, 0, 0)


class Ball(pygame.sprite.Sprite):
    # This class represents a ball. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(PINK)
        self.image.set_colorkey(PINK)

        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

    #tried to make the ball a heart but couldn't get the code to work, to even test out if the shape was right
        #pygame.draw.polygon(self.image, color, [(width, height), (width+5, height-5), (width+10, height), (width+20, height-5), (width-5, height-5), (width+5, height-15)])

        self.velocity = [randint(4, 8), randint(-8, 8)]

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        #self.polygon = self.image.get_polygon()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)