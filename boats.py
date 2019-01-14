import pygame

class Ship(pygame.sprite.Sprite):
    """ A basic ship """
    def __init__(self, gridpos, blocksize, shipsize):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((blocksize[0]*shipsize[0], blocksize[1]*shipsize[1]))
        self.rect = self.image.get_rect()
        self.x = gridpos[0]; self.y = gridpos[1]
        self.hurt = 0; self.dead = False
        self.blocksize = blocksize
        self.shipsize = shipsize
        self.image.fill((0,0,0))
        self.type = 'ship'
        self.accounted = False # for verbose purposes

    def turn(self):
        self.image = pygame.Surface((self.image.get_height(), self.image.get_width()))
        self.image.fill((0,0,0))
        x = self.x; y = self.y
        self.rect = self.image.get_rect()
        self.rect.x = x; self.rect.y = y
        self.x = self.rect.x; self.y = self.rect.y
        del x, y

    def hit(self):
        self.hurt += 1
        if self.hurt >= self.shipsize[0] and\
           self.hurt >= self.shipsize[1]:
            self.dead = True

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

class AircraftCarrier(Ship):
    """ The aircraft carrier """
    def __init__(self, gridpos, blocksize):
        Ship.__init__(self, gridpos, blocksize, (1,5))
        self.type = 'Aircraft Carrier'

class Battleship(Ship):
    """ The battleship """
    def __init__(self, gridpos, blocksize):
        Ship.__init__(self, gridpos, blocksize, (1,4))
        self.type = 'Battleship'

class Destroyer(Ship):
    """ The destroyer """
    def __init__(self, gridpos, blocksize):
        Ship.__init__(self, gridpos, blocksize, (1,3))
        self.type = 'Destroyer'

class Submarine(Ship):
    """ The submarine """
    def __init__(self, gridpos, blocksize):
        Ship.__init__(self, gridpos, blocksize, (1,3))
        self.type = 'Submarine'

class PatrolBoat(Ship):
    """ The patrol boat """
    def __init__(self, gridpos, blocksize):
        Ship.__init__(self, gridpos, blocksize, (1,2))
        self.type = 'Patrol Boat'
