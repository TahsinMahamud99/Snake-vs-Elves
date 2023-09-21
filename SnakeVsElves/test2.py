import pygame
import pygame as pygame

from config import*

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('test2')

x = 50
y = 50

width = 16
height = 16
height = 60
vel = 8
direction = None
run = True

class Player():
    def __init__(self):

        self.x = 0
        self.y = 0
        self.direction = 'left'
        self.vel = 5

    def player_input(self):

        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_LEFT]:
            self.direction = 'left'
        elif self.keys[pygame.K_RIGHT]:
            self.direction = 'right'

        elif self.keys[pygame.K_UP]:
            self.direction = 'up'

        elif self.keys[pygame.K_DOWN]:
            self.direction = 'down'

    def player_motion(self):

        if self.direction == 'left':
            self.x -= self.vel
        elif self.direction == 'right':
            self.x += self.vel
        elif self.direction == 'up':
            self.y -= self.vel
        elif self.direction == 'down':
            self.y += self.vel

while run:
    win.fill(BLUE)
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #check input
    player = Player()
    player.player_input()
    player.player_motion()



    enemy = pygame.Surface([length, length])
    box = pygame.Surface([length, length])
    #rect1 = box.get_rect()
    box.fill(RED)
    enemy.fill(GREEN)
    #rect2 = enemy.get_rect()

    rect1 = win.blit(enemy, (80, 80))

    rect2 = win.blit(box, (x, y) )
    #pygame.draw.rect(win, (YELLOW), (x, y, length, length))

    if rect1.colliderect(rect2):
        pygame.draw.rect(win, WHITE, (200, 200, 100, 100))
        #box_list[[x,]]
    pygame.display.update()