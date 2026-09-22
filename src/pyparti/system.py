import random as random


class ParticleSystem:
    def __init__(self):
        self.particles: list = []  # Container for all the particles

    # Update all particles and remove dead ones
    def update(self):
        for p in self.particles[:]:
            p.update()
            if not p.is_alive():
                self.particles.remove(p)

    # Draws all particles onto the window
    def draw(self, screen):
        for p in self.particles:
            p.draw(screen)
