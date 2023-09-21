import pygame
import spritesheet
from animationSprites import AnimationSprites
from config import*
import random

pygame.init()

class SpriteSheet():
    def __init__(self, image, win):
        self.sheet = image
        self.win = win

    def get_image(self, frame, width = 16, height = 16, scale = 1, colour = RED):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)

        return image

    def create_sprite_list(self, image_variable, animation_steps, step_counter):
        animation_list = []

        for animation in animation_steps:
            temp_img_list = []
            for _ in range(animation):
                temp_img_list.append(image_variable.get_image(step_counter, 16, 16, 6, RED))
                step_counter += 1
            animation_list.append(temp_img_list)

    def create_animation_list(self, animation_list=[], animation_steps=[4, 4, 4, 4],
                              action=0, step_counter=0, animation_cooldown=100, frame=0):

        self.animation_list = animation_list
        self.animation_steps = animation_steps
        self.action = action
        self.step_counter = step_counter
        self.frame = frame
        self.animation_cooldown = animation_cooldown

        #return self.animation_list, self.animation_steps, self.action, self.step_counter, self.frame, self.animation_cooldown

    def create_sprite_list(self):
        animation_list = self.create_animation_list()[0]
        animation_steps = self.create_animation_list()[1]
        step_counter = self.create_animation_list()[2]
        animation_steps = self.create_animation_list()[3]
        animation_cooldown = self.create_animation_list()[3]

        for animation in animation_steps:
            temp_img_list = []
            for _ in range(animation):
                temp_img_list.append(
                    self.sprite_sheet.get_image(step_counter, player_width, player_height, scale_factor, RED))
                step_counter += 1
            animation_list.append(temp_img_list)

    def update_animation(self, animation_steps, animation_cooldown):
        global last_update
        global frame
        global action

        self.animation_cooldown = animation_cooldown
        self.animation_steps = animation_steps

        current_time = pygame.time.get_ticks()

        if current_time - last_update >= animation_cooldown:
            frame = (frame + 1) % animation_steps[action]
            last_update = current_time

        self.win.blit(self.animation_list[action][frame], (self.player_x, self.player_y))