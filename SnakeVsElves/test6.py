import pygame
from config import*
from pygame.locals import*
from player import Player
from enemies import Enemy

class Game():

    def __init__(self):

        self.win = pygame.display.set_mode((500, 500))
        self.player = Player(self.win)
        self.player.create_snake()
        self.enemy = Enemy(self.win, 'npc')
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:

            self.win.fill(BLUE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.current_time = pygame.time.get_ticks()

            #SNAKE
            self.player.draw_snake(self.current_time)
            self.player.player_input(self.current_time)
            self.player.player_motion(self.current_time)

            #ENEMY
            self.enemy_behaviour()

            self.collision_snake_enemy()

            self.clock.tick(30)

            pygame.display.update()

    def collision_snake_enemy(self):
        if self.player.head_snake.colliderect(self.enemy.a) & self.enemy.enemy_alive:
            self.enemy.enemy_alive = False
            pygame.draw.rect(self.win, (255, 255, 255), (10, 10, 50, 50))
            self.player.increase_size()
    def enemy_behaviour(self):
        if self.enemy.enemy_alive == True:
            self.enemy.draw_enemy()
            self.enemy.npc_movement(self.current_time)

