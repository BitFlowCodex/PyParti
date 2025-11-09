import pygame as pg
import random as random

class Particle():
    def __init__(
        self, 
        x: float,
        y: float,
        duration: float,
        color: str
    ) -> None:

        self.x = x
        self.y = y
        self.color = color
        self.lifeTime = duration
        self.age = 0
        self.veloX = random.uniform(-x+10,x)
        self.veloY = random.uniform(-y+10,y)
        
    def Generate(self):
        self.x = self.veloX
        self.y = self.veloY
        self.age += 1
    
    def is_alive(self):
        return True if age >= lifeTime else False 
