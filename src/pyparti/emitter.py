from .particle import Particle


class Emitter:
    def __init__(
        self, particle_list: list, particle: object, amount: int = 5, velocity=None
    ):
        self.particle = particle
        self.amount = amount
        self.particle_list = particle_list
        self.velocity = velocity

    def emit(self):
        for _ in range(self.amount):
            
            new_particle = Particle(
                x=self.particle.x,
                y=self.particle.y,
                velocity=(self.velocity() if self.velocity else self.particle.velocity),
                lifeTime=self.particle.lifeTime,
                color=self.particle.color,
                hasGravity=self.particle.hasGravity,
                delta=self.particle.delta,
            )
            self.particle_list.append(new_particle)
