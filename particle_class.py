import pygame as pg
import random as random

class Particle():
    def __init__(
        self, 
        x: float,
        y: float,
        duration: float,
        color: str | tuple,
        size: float 
    ) -> None:

        self.x = x
        self.y = y
        self.color = color
        self.lifeTime = duration
        self.size = size
        self.age = 0.0

        # Fixed velocity range
        self.veloX = random.uniform(-5,5)
        self.veloY = random.uniform(-5,5)
        
    def update(self):
        self.x += self.veloX
        self.y += self.veloY
        self.age += 0.1
        self.size -= self.age

    def draw(self, surface):
        pg.draw.rect(surface, self.color, (self.x,self.y, self.size, self.size))
    
    def is_alive(self):
        return True if self.age < self.lifeTime else False 
