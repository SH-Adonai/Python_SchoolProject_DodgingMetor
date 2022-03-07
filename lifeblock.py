import pygame

class Lifeblock:
    def __init__(self, pos, line):
        self.pos = pos
        self.line = line
        self.color = (139,0,0)

    def update_and_drawl(self, screen):
        pygame.draw.rect(screen, self.color, self.pos, self.line)