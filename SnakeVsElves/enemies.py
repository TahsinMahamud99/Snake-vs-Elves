import pygame
import spritesheet
from animationSprites import AnimationSprites
from config import*
import random


class Enemy():
    def __init__(self, win, x = 32*10, y = 32*10):
        self.win = win
        self.frame = 0

        self.x = x
        self.y = y
        self.direction = 'right'
        self.vel = 32
        self.size = 32
        self.enemy_alive = True
        self.seen = False

        self.enemy_block = pygame.image.load('img/snake/enemy_block.png')

        #how many steps it will move right, down, left and then up (random number)
        self.npc_motion_range = [0, 0, 0, 0]
        # to track how many steps it has moved right, down, left and then up
        self.npc_movement_count = [0, 0, 0, 0]

        # time delay variables
        self.time_skip = 600
        self.static_time = 0



        #enemy_vision_range
        self.visibility = 30
        self.visibility_box_size = 32
        #coordinates of vision range
        self.x_visibility_box = x - self.visibility_box_size * 2
        self.y_visibility_box = y - self.visibility_box_size * 2
        #size of vision range
        self.box_height = self.size * 3
        self.box_width = self.size * 2

        #score variables
        self.points = 0
        self.static_time1 = 0

        #creating vision range rectangle
        self.visibility_box = pygame.Rect(self.x_visibility_box, self.y_visibility_box, self.box_height, self.box_width )

        self.exclamation = pygame.image.load("img/others/pixil-frame-0 (9).png")

    def sees_snake(self):
        if self.direction == 'up':
            self.direction = 'down'

        elif self.direction == 'down':
            self.direction = 'up'

        elif self.direction == 'left':
            self.direction = 'right'

        elif self.direction == 'right':
            self.direction = 'left'




    def draw_visibility_box(self):
        if self.enemy_alive == True:
            if self.direction == 'up':

                self.box_width = self.size * 3
                self.box_height = self.size * 2

                self.x_visibility_box = self.x - self.box_width / 3
                self.y_visibility_box =  self.y - self.box_height

            elif self.direction == 'down':

                self.box_width = self.size * 3
                self.box_height = self.size * 2


                self.x_visibility_box = self.x - self.box_width / 3
                self.y_visibility_box = self.y + self.size
            elif self.direction == 'left':

                self.box_height = self.size * 3
                self.box_width = self.size * 2

                self.x_visibility_box = self.x - self.size*2
                self.y_visibility_box = self.y - self.box_height/3
            elif self.direction == 'right':

                self.box_height = self.size * 3
                self.box_width = self.size * 2

                self.x_visibility_box = self.x + self.size
                self.y_visibility_box = self.y - self.box_height/3

            self.visibility_box = pygame.Rect(self.x_visibility_box, self.y_visibility_box, self.box_width, self.box_height )

            pygame.draw.rect(self.win, (LIGHT_GREEN), self.visibility_box)
            #pygame.display.update()
            #self.rect = self.win.blit(self.visibility_box, (self.x_visibility_box, self.y_visibility_box))

    def npc_movement(self, current_time):

        self.current_time = current_time
        if self.current_time - self.static_time > self.time_skip:
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

    def set_npc_movement_range(self):
        self.npc_motion_range = [random.randint(0, 5), random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)]

    def reset_count(self):
        self.npc_movement_count = [0, 0, 0, 0]

    def draw_enemy(self, current_time):
        self.current_time = current_time
        self.rect_enemy = self.enemy_block.get_rect()
        self.animate(self.current_time)


    def npc_movement_right(self):
        self.direction = 'right'
        self.x += self.vel


    def npc_movement_left(self):
        self.direction = 'left'
        self.x -= self.vel


    def npc_movement_down(self):
        self.direction = 'down'
        self.y += self.vel


    def npc_movement_up(self):
        self.direction = 'up'
        self.y -= self.vel

    def keep_moving(self, current_time):
        self.time_skip = 300
        self.current_time = current_time
        if self.current_time - self.static_time > self.time_skip:
            self.static_time = self.current_time
            if self.direction == 'right':
                self.x += self.vel
            elif  self.direction == 'left':
                self.x -= self.vel
            elif self.direction == 'up':
                self.y -=self.vel
            elif self.direction == 'down':
                self.y +=self.vel
    def reset_enemy(self):
        if self.enemy_alive == False:
            self.x = random.randrange(0, WIDTH - self.size, 32)
            self.y = random.randrange(0, HEIGHT - self.size, 32)
            self.time_skip = 600
            self.enemy_alive = True
            self.seen = False
    def load_sprites(self):

        self.down_sprite = [pygame.image.load('img/elf/pixil-frame-0.png').convert_alpha(), pygame.image.load('img/elf/pixil-frame-1.png').convert_alpha(),
                     pygame.image.load('img/elf/pixil-frame-2.png').convert_alpha(), pygame.image.load('img/elf/pixil-frame-3.png').convert_alpha()]
        self.right_sprite = [pygame.image.load('img/elf/pixil-frame-4.png').convert_alpha(), pygame.image.load('img/elf/pixil-frame-5.png').convert_alpha(),
                     pygame.image.load('img/elf/pixil-frame-6.png').convert_alpha(), pygame.image.load('img/elf/pixil-frame-7.png').convert_alpha()]

        self.left_sprite = [pygame.image.load('img/elf/pixil-frame-8.png').convert_alpha(), pygame.image.load('img/elf/pixil-frame-9.png').convert_alpha(),
                     pygame.image.load('img/elf/pixil-frame-10.png').convert_alpha(), pygame.image.load('img/elf/pixil-frame-11.png').convert_alpha()]

        self.up_sprite = [pygame.image.load('img/elf/pixil-frame-12.png').convert_alpha(), pygame.image.load('img/elf/pixil-frame-13.png').convert_alpha(),
                     pygame.image.load('img/elf/pixil-frame-14.png').convert_alpha(), pygame.image.load('img/elf/pixil-frame-15.png').convert_alpha()]
    def animate(self, current_time):

        current_time
        self.load_sprites()
        if self.seen == True:
            self.win.blit(pygame.transform.scale_by(self.exclamation, 2), (self.x, self.y - 32))
            time_skip = 500
        else:
            time_skip = 600

        if self.frame < 4:
            if self.direction == 'up':
                self.a = self.win.blit(pygame.transform.scale_by(self.up_sprite[self.frame], 2), (self.x, self.y))

            elif self.direction == 'down':
                self.a = self.win.blit(pygame.transform.scale_by(self.down_sprite[self.frame], 2),(self.x, self.y))

            elif self.direction == 'left':
                self.a = self.win.blit(pygame.transform.scale_by(self.left_sprite[self.frame], 2), (self.x, self.y))

            elif self.direction == 'right':
                self.a = self.win.blit(pygame.transform.scale_by(self.right_sprite[self.frame], 2), (self.x, self.y))

            if current_time - self.static_time1 > time_skip:
                self.static_time1 = current_time
                self.frame +=1
        else:
            self.frame = 0
    def increase_points(self):
        if self.enemy_alive == False:
            self.points += 5






