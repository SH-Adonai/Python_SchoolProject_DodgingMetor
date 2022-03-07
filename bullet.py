import pygame

class Bullet:
    def __init__(self, x,y, to_x, to_y, type):
        self.pos = [x,y]
        self.to = [to_x, to_y]
        self.radius = [7, 10, 5, 13]
        self.color = [(190,0,0), (0,190,0), (130,80,0), (30,10,225)]
        self.type = type

    def update_and_drawb(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + dt*self.to[0]*0.5)%width
        self.pos[1] = (self.pos[1] + dt*self.to[1]*0.5)%height
        pygame.draw.circle(screen, self.color[self.type], self.pos, self.radius[self.type])