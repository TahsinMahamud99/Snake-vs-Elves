import pygame
from config import*
import random

win = pygame.display.set_mode((500, 500))

x = 0
y = 0

class Enemy():
    def __init__(self, win, enemy_type = 'npc'):
        self.win = win
        self.enemy_type = enemy_type
        self.x = 160
        self.y = 160
        self.direction = 'right'
        self.vel = 16
        self.size = 16
        self.count = 0
        self.enemy_block = pygame.image.load('img/snake/enemy_block.png')
        self.npc_motion_range = [0, 0, 0, 0]
        self.npc_movement_count = [0, 0, 0, 0]
        self.static_time = 0

    def npc_movement(self, current_time):

        self.current_time = current_time
        if self.current_time - self.static_time > 600:
            self.static_time = self.current_time
            if self.npc_movement_count[0] < self.npc_motion_range[0]:
                self.npc_movement_right()
                self.npc_movement_count[0] += 1
            elif self.npc_movement_count[1] < self.npc_motion_range[1]:

                self.npc_movement_down()
                self.npc_movement_count[1] += 1
            elif self.npc_movement_count[2] < self.npc_motion_range[2]:

                self.npc_movement_left()
                self.npc_movement_count[2] += 1
            elif self.npc_movement_count[3] < self.npc_motion_range[3]:
                self.npc_movement_up()
                self.npc_movement_count[3] += 1
            else:
                self.set_npc_movement_range()
                self.reset_count()

        #pygame.display.update()


    def set_npc_movement_range(self):
        self.npc_motion_range = [random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)]

    def reset_count(self):
        self.npc_movement_count = [0, 0, 0, 0]

    def draw_enemy(self):
        self.a = win.blit(self.enemy_block, (self.x, self.y))
        #self.rect_enemy = self.a.get_rect()

    def get_count(self):
        self.count += 1

    def npc_movement_right(self):
        self.direction = 'right'
        self.x += self.vel
        self.count += 1


    def npc_movement_left(self):
        self.direction = 'left'
        self.x -= self.vel
        self.count += 1


    def npc_movement_down(self):
        self.direction = 'down'
        self.y += self.vel
        self.count += 1


    def npc_movement_up(self):
        self.direction = 'up'
        self.y -= self.vel
        self.count += 1



class Player():
    def __init__(self, win):
        self.win = win
        self.x = 0
        self.y = 0
        self.direction = 'right'
        self.vel = 16
        self.size = 16
        self.length = 3
        self.box = pygame.image.load('img/snake/block.png')
        self.boxes = []
        self.a = [self.x, self.y]
        self.head_left = pygame.image.load('img/snake/pixil-frame-0.png')
        self.head_right = pygame.image.load('img/snake/pixil-frame-1.png')
        self.head_up = pygame.image.load('img/snake/pixil-frame-3.png')
        self.head_down = pygame.image.load('img/snake/pixil-frame-2.png')
        self.body = pygame.image.load('img/snake/pixil-frame-4.png')
        self.static_time = 0


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

    def player_motion(self, current_time):
        self.current_time = current_time
        if self.current_time - self.static_time > 140:
            self.static_time = self.current_time
            self.update_motion(self.current_time)


            if self.direction == 'left':
                self.boxes[0][0] -= self.vel
            elif self.direction == 'right':
                self.boxes[0][0] += self.vel

            elif self.direction == 'up':
                self.boxes[0][1] -= self.vel
            elif self.direction == 'down':
                self.boxes[0][1] += self.vel

    def create_snake(self):

        for i in range(self.length):
            self.boxes.append([self.x, self.y])
            self.x += self.size
        #print(self.boxes)

    def draw_snake(self, current_time):
        self.current_time = current_time

        for i in range(self.length):
            if i == 0:
                self.head_snake = win.blit(self.box, (self.boxes[i][0], self.boxes[i][1]))
            elif i == self.length - 1:
                self.tail = win.blit(self.box, (self.boxes[i][0], self.boxes[i][1]))
            else:
                self.body = win.blit(self.box, (self.boxes[i][0], self.boxes[i][1]))


    def update_motion(self, current_time):
        if self.current_time - self.static_time > 600:
            self.static_time = self.current_time
        for i in range(self.length - 1, 0, -1):
            self.boxes[i][0] = self.boxes[i-1][0]
            self.boxes[i][1] = self.boxes[i - 1][1]
            print(self.boxes)


player = Player(win)
player.create_snake()
enemy = Enemy(win, 'npc')
clock = pygame.time.Clock()

run = True
while run:
    win.fill(BLUE)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    current_time = pygame.time.get_ticks()

    #SNAKE
    player.draw_snake(current_time)
    player.player_input()
    player.player_motion(current_time)

    #ENEMY
    enemy.draw_enemy()
    enemy.npc_movement(current_time)

    if player.head_snake.colliderect(enemy.a):
        pygame.draw.rect(win, (255, 255, 255), (10, 10, 50, 50))

    clock.tick(30)
    pygame.display.update()