import pygame as pg
import random as random

class Particle():
    def __init__(
        self, 
        x: float,
        y: float,
        duration: float = 3.0,
        color: str | tuple = "white",
        size: float = 10.0,
        is_gravity: bool = False
    ) -> None:
        
        self.x = x
        self.y = y
        self.color = color
        self.lifeTime = duration
        self.size = size
        self.is_gravity = is_gravity
        self.age = 0.0
    
        # Pre-made surface for the particle (fast to draw)
        self.surface = pg.Surface((self.size,self.size))
        self.surface.fill(self.color)
    
        # Fixed velocity range
        self.veloX = random.uniform(-5,5)
        self.veloY = random.uniform(-5,5)
        
    def update(self):
        # Move particle based on velocity
        self.x += self.veloX
        if self.is_gravity:
            self.veloY += 0.5 # Gravity acceleration
        self.y += self.veloY
        
        # Age particle and shrink size
        self.age += 0.1

    def draw(self, screen):
        # Draw the particle onto the screen
        screen.blit(self.surface, (self.x, self.y))
  
    def is_alive(self):
        # Check if particle lifetime is still active
        return self.age < self.lifeTime



class ParticleSystem:
    def __init__(self) -> None:
        # Container for all the particles
        self.particles: list = []
    
    def emit(self, x: float, y: float, amount=10, **kwargs):
        # Spawn multiple particles at once
        for _ in range(amount):
            self.particles.append(Particle(x, y, **kwargs))

    def update(self):
        # Update all particles and remove dead ones
        for p in self.particles[:]:
            p.update()
            if not p.is_alive():
                self.particles.remove(p)

    def draw(self, screen):
        # Draw all particles
        for p in self.particles:
            p.draw(screen)
