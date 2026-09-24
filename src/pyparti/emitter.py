from .particle import Particle
from pygame import Vector2
from random import uniform


class Emitter:
    def __init__(
        self,
        particleList: list,
        particle: object,
        amount: int = 5,
        delay: float = 0,
    ):
        self.particle = particle
        self.amount = amount
        self.particleList = particleList
        self.delay = delay
        self.timer = 0

    def update(self, dt):
        self.timer -= dt

        if self.timer <= 0:
            self.emit()
            self.timer = self.delay

    def emit(self):
        width, height = self.particle.size

        for _ in range(self.amount):
            newParticle = Particle(
                position=self.particle.position.copy(),
                velocityRange=self.particle.velocityRange,
                lifeTime=self.particle.lifeTime,
                color=self.particle.color,
                size=(width, height),
                gravity=self.particle.gravity,
                shape=self.particle.shape,
            )

            xRange, yRange = newParticle.velocityRange

            newParticle.velocity = Vector2(
                uniform(*xRange),
                uniform(*yRange),
            )

            self.particleList.append(newParticle)
