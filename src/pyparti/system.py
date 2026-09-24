class ParticleSystem:
    def __init__(self):
        self.particles: list = []

    # Updates all particles and removes dead ones
    def update(self, delta):
        for particle in self.particles[:]:
            particle.update(delta)

            if not particle.is_alive():
                self.particles.remove(particle)

    # Draws all particles onto the window
    def draw(self, screen):
        for particle in self.particles:
            particle.draw(screen)
