import pygame

class Player():
    def __init__(self, win):
        self.win = win
        self.x = 32*3
        self.y = 32*3
        self.vel = 32
        self.size = 32
        self.length = 3
        self.direction = 'right'


        self.box = pygame.image.load('img/snake/block.png')

        #list storing all the rectangle coordinates making the snake
        self.boxes = []
        self.a = [self.x, self.y]

        # snake sprites
        self.head_left = pygame.image.load('img/snake/pixil-frame-2.png')
        self.head_right = pygame.image.load('img/snake/pixil-frame-3.png')
        self.head_up = pygame.image.load('img/snake/pixil-frame-0.png')
        self.head_down = pygame.image.load('img/snake/pixil-frame-1.png')
        self.body_tail = pygame.image.load('img/snake/pixil-frame-4.png')


        self.static_time = 0
        self.time_interval = 200

    # Snake dashes when pressing spaceBar
    def dash(self, dash_status):
        if dash_status:
            self.time_interval = 30
        else:
            self.time_interval = 140


    def player_input(self, keys, dash_status):#event_key, dash_status):
        self.keys = keys
        if keys[pygame.K_SPACE]:
            dash_status = True
        self.dash(dash_status)
        if keys[pygame.K_UP] and self.direction != 'down':
            self.direction = 'up'
        elif keys[pygame.K_DOWN] and self.direction != 'up':
            self.direction = 'down'
        elif keys[pygame.K_LEFT] and self.direction != 'right':
            self.direction = 'left'
        elif keys[pygame.K_RIGHT] and self.direction != 'left':
            self.direction = 'right'


    def player_motion(self, current_time):
        #Animation delay
        self.current_time = current_time
        if self.current_time - self.static_time > self.time_interval:
            self.static_time = self.current_time
            self.update_motion()

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

    def draw_snake(self, current_time):
        self.current_time = current_time
        for i in range(self.length):
            if i == 0:
                self.head_snake = self.win.blit(self.box, (self.boxes[i][0], self.boxes[i][1]))
            elif i == self.length - 1:
                self.tail = self.win.blit(self.box, (self.boxes[i][0], self.boxes[i][1]))
            else:
                self.body = self.win.blit(self.box, (self.boxes[i][0], self.boxes[i][1]))


    def update_motion(self):

        for i in range(self.length - 1, 0, -1):
            self.boxes[i][0] = self.boxes[i-1][0]
            self.boxes[i][1] = self.boxes[i - 1][1]
            print(self.boxes)

    def increase_size(self):
        self.length += 1
        self.x = self.boxes[self.length-2][0]
        self.y += self.boxes[self.length-2][1]
        self.boxes.append([self.x, self.y])

    def player_sprite(self):
        for i in range(self.length):
            # HEAD
            if i == 0:
                if self.direction == 'up':
                    self.win.blit(pygame.transform.scale_by(self.head_up, 2), (self.boxes[i][0], self.boxes[i][1]))
                elif self.direction == 'down':
                    self.win.blit(pygame.transform.scale_by(self.head_down, 2), (self.boxes[i][0], self.boxes[i][1]))
                elif self.direction == 'left':
                    self.win.blit(pygame.transform.scale_by(self.head_left, 2), (self.boxes[i][0], self.boxes[i][1]))
                elif self.direction == 'right':
                    self.win.blit(pygame.transform.scale_by(self.head_right, 2), (self.boxes[i][0], self.boxes[i][1]))
            # BODY
            else:
                self.win.blit(pygame.transform.scale_by(self.body_tail, 2), (self.boxes[i][0], self.boxes[i][1]))




