import pygame
import spritesheet
from config import*


class AnimationSprites():
    def __init__(self, screen, img_location = "img/snake/snaky.png", animation_steps = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], height = 16, width = 16, scale_factor = 3, x = 0, y = 0):
        self.sprite_sheet_image = pygame.image.load(img_location).convert_alpha()
        self.sprite_sheet = spritesheet.SpriteSheet(self.sprite_sheet_image)
        # create animation_list
        self.animation_list = []
        self.animation_steps = animation_steps
        self.action = 1
        self.last_update = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()
        self.animation_cooldown = 500
        self.frame = 0
        self.step_counter = 0
        self.screen = screen
        self.animation_steps = animation_steps
        self.height = height
        self.width = width
        self.scale_factor = scale_factor
        self.x = x
        self.y = y
    def create_spritelist(self):
        for animation in self.animation_steps:
            temp_img_list = []
            for _ in range(animation):
                temp_img_list.append(self.sprite_sheet.get_image(self.step_counter, self.height, self.width, self.scale_factor, RED))
                self.step_counter += 1
            self.animation_list.append(temp_img_list)
    def update_animation(self, action = 1, x = 0, y = 0):
        self.x = x
        self.y = y
        if self.current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = self.current_time
            if self.frame >= len(self.animation_list[action]):
                self.frame = 0

        # show frame image
        self.screen.blit(self.animation_list[action][self.frame], (self.x, self.y))
