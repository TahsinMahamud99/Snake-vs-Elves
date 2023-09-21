import pygame
from config import*


class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, colour):
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