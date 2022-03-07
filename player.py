import pygame

class Player:
    def __init__(self,x,y):
        self.image = pygame.image.load('C:\이선휘\Programming\Python\GuaSoSa\PYGAME\\player.png')
        self.image = pygame.transform.scale(self.image, (32,32))
        self.invisible = pygame.image.load('C:\이선휘\Programming\Python\GuaSoSa\PYGAME\\nothing.png')
        self.pos = [x,y]
        self.to = [0,0]
        self.angle = 0

    def draw(self, screen):
        if self.to == [-1,-1]: self.angle = 45
        elif self.to == [-1,0]: self.angle = 90
        elif self.to == [-1,1]: self.angle = 135
        elif self.to == [0,1]: self.angle = 180
        elif self.to == [1,1]: self.angle = 225
        elif self.to == [1,0]: self.angle = 270
        elif self.to == [0,-1] : self.angle = 0

        rotated_image = pygame.transform.rotate(self.image, self.angle)
        
        calib_pos = ( self.pos[0] - rotated_image.get_width()/2, self.pos[1] - rotated_image.get_width()/2)
        
        screen.blit(rotated_image,calib_pos )
    
    def indraw(self,screen):
        if self.to == [-1,-1]: self.angle = 45
        elif self.to == [-1,0]: self.angle = 90
        elif self.to == [-1,1]: self.angle = 135
        elif self.to == [0,1]: self.angle = 180
        elif self.to == [1,1]: self.angle = 225
        elif self.to == [1,0]: self.angle = 270
        elif self.to == [0,-1] : self.angle = 0

        rotated_image = pygame.transform.rotate(self.invisible, self.angle)
        
        calib_pos = ( self.pos[0] - rotated_image.get_width()/2, self.pos[1] - rotated_image.get_width()/2)
        
        screen.blit(rotated_image,calib_pos )


    def update(self, dt, screen):
        width, height = screen.get_size()
        self.pos[0] = (self.pos[0] + (self.to[0]*dt*0.3))
        self.pos[1] = (self.pos[1] + (self.to[1]*dt*0.3))
        self.pos[0] = min(max(self.pos[0], 16), width -16)
        self.pos[1] = min(max(self.pos[1], 16), height -16)


    def goto(self, x,y):
        self.to[0] += x
        self.to[1] += y