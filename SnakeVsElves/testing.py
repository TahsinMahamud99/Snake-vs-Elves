import pygame
from config import*
from pygame.locals import*

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    run = True
    length = 16
    scale_factor = 3
    x = 0
    y = 0
    while run:
        #screen.fill(BLUE)
        #pygame.display.update()
        run = True
        screen.fill(BLUE)

        pygame.draw.rect(screen, YELLOW, (x, y, length, length))

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
                if event.key == K_UP:
                    y -= y
                    #pygame.draw.rect(screen, YELLOW, (x, y, length, length))
                if event.key == K_DOWN:
                    y += y
                    #pygame.draw.rect(screen, YELLOW, (x, y, length, length))
                if event.key == K_LEFT:
                    x -= x
                    #pygame.draw.rect(screen, YELLOW, (x, y, length, length))
                if event.key == K_RIGHT:
                    x +=x
                    #pygame.draw.rect(screen, YELLOW, (x, y, length, length))


            elif event.type == pygame.QUIT:
                run = False
        pygame.draw.rect(screen, YELLOW, (x, y, length, length))




if __name__ == '__main__':
 main()