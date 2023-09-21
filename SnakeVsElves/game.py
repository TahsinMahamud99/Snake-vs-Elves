import pygame
from config import*
from pygame.locals import*
from player import Player
from enemies import Enemy
from os import path
from maps import  TiledMap

pygame.init()


class Game():

    def __init__(self):

        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.player = Player(self.win)
        self.player.create_snake()
        self.enemy = Enemy(self.win)
        self.clock = pygame.time.Clock()
        self.running = True
        self.dash_status = False
        self.font = pygame.font.Font('fonts/Upheaval/UpheavalPro.ttf', 32)
        self.text = f'SCORE {self.enemy.points}'
        self.score_count = 0
        self.map = TiledMap(self.win, map1)
        #self.bg = pygame.image.load('img/snake/grass (2).png')
        #self.bg = pygame.transform.scale(self.bg, (WIDTH, HEIGHT))


    def run(self):
        while self.running:

            self.win.fill(GRASS)
            self.map.put_tile()
            #self.draw_grid()
            self.score(self.text, self.font, (0, 0, 0), 10, 10)

            #self.win.blit(self.bg, (0, 0))


            self.current_time = pygame.time.get_ticks()

            #ENEMY
            #draws enemy vision
            self.enemy.reset_enemy()
            self.enemy.draw_visibility_box()
            #self.enemy.load_sprites()

            #manages enemie's behaviour
            self.enemy_behaviour()

            #SNAKE
            #draws snake on screen
            self.player.draw_snake(self.current_time)

            self.player.player_sprite()
            #updates motion of player based on input
            self.player.player_motion(self.current_time)
            #checks for collision between snake and enemy for snake to eat enemy
            self.collision_snake_enemy()
            self.collision_player_player()

            #checks if enmy has seen snake
            self.collision_seen()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                keys = pygame.key.get_pressed()
                #takes in the input of the player
                self.player.player_input(keys, self.dash_status)

            self.current_time = pygame.time.get_ticks()

            self.snake_collide_wall()


            self.clock.tick(30)

            pygame.display.update()

    def collision_snake_enemy(self):
        if self.player.head_snake.colliderect(self.enemy.a) & self.enemy.enemy_alive:
            self.enemy.enemy_alive = False
            pygame.draw.rect(self.win, (255, 255, 255), (10, 10, 50, 50))
            self.player.increase_size()
    def collision_player_player(self):
        if self.player.head_snake.colliderect(self.player.body):
            self.win.blit(self.player.head_up, (90, 90))

    def collision_seen(self):
        if self.player.head_snake.colliderect(self.enemy.visibility_box):
            self.enemy.sees_snake()
            self.enemy.seen = True
            pygame.draw.rect(self.win, (255, 255, 255), (80, 100, 50, 50))

    def enemy_behaviour(self):
        if self.enemy.enemy_alive == True:
            self.enemy.draw_enemy(self.current_time)
            if self.enemy.seen == False:
                self.enemy.npc_movement(self.current_time)
            else:
                self.enemy.keep_moving(self.current_time)

    def score(self, text, font, text_col = WHITE, x = 10, y = 10):

        self.enemy.increase_points()

        text = font.render(f'SCORE : {self.enemy.points}', True, (0, 0, 0))
        self.he = pygame.image.load('img/snake/slab.png')
        self.he = pygame.transform.scale(self.he, (WIDTH, 64))
        self.win.blit(self.he, (0, 0))
        self.win.blit(text, (WIDTH - text.get_width() - 32, 20))


    '''def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.win, WHITE, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.win, WHITE, (0, y), (WIDTH, y))'''
    def snake_collide_wall(self):
        if self.map.obstacle.colliderect(self.player.head_snake):
            self.rectangle = pygame.draw.rect(self.win, WHITE, (100, 100, 2000, 80))
            self.win.blit(pygame.transform.scale_by(self.player.head_up, 10), (200, 200))
            print("COLLLLLLIIIIDE")




