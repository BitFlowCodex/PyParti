from .particle import Particle
from pygame import Vector2


class Emitter:
    def __init__(
        self,
        particleList: list,
        particle: object,
        amount: int = 5,
        velocity=None,
        delay: float = 0,
    ):
        self.particle = particle
        self.amount = amount
        self.particleList = particleList
        self.velocity = velocity
        self.delay = delay
        self.timer = 0

    def update(self, dt):
        self.timer -= dt

        if self.timer <= 0:
            self.emit()
            self.timer = self.delay

    def emit(self):
        for _ in range(self.amount):

            newParticle = Particle(
                x=self.particle.x,
                y=self.particle.y,
                velocity=(self.velocity() if self.velocity else self.particle.velocity),
                lifeTime=self.particle.lifeTime,
                color=self.particle.color,
                hasGravity=self.particle.hasGravity,
                delta=self.particle.delta,
            )
            self.particleList.append(newParticle)
