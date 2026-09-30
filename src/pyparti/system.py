import pygame as pg
from .particle import Particle


class ParticleSystem:
    def __init__(self, max_particles=5000):
        self.max_particles = max_particles

        # Create particle ONCE
        self.particles = [Particle() for _ in range(max_particles)]

        self.active = []

        self.free = list(range(max_particles))

        self.emitters = []

        self.image_cache = {}

    def _get_image(self, shape, size, color):
        width = max(1, int(size[0]))
        height = max(1, int(size[1]))

        if isinstance(color, pg.Color):
            color = tuple(color)

        key = (shape, width, height, color)

        image = self.image_cache.get(key)

        if image is not None:
            return image

        image = pg.Surface(
            (width, height),
            pg.SRCALPHA,
        )

        rect = image.get_rect()

        if shape == "rect":
            pg.draw.rect(
                image,
                color,
                rect,
                border_radius=2,
            )

        elif shape == "ellipse":
            pg.draw.ellipse(
                image,
                color,
                rect,
            )

        elif shape == "circle":
            radius = min(width, height) // 2

            pg.draw.circle(
                image,
                color,
                (width // 2, height // 2),
                radius,
            )

        else:
            raise ValueError(f"Unknown particle shape: {shape}")

        self.image_cache[key] = image

        return image

    def spawn(
        self,
        *,
        x,
        y,
        vx,
        vy,
        lifetime,
        gravity,
        shape,
        size,
        color,
    ):
        if not self.free:
            return False

        index = self.free.pop()

        particle = self.particles[index]

        image = self._get_image(shape, size, color)

        particle.reset(
            x=x,
            y=y,
            vx=vx,
            vy=vy,
            lifetime=lifetime,
            gravity=gravity,
            image=image,
        )

        self.active.append(index)

        return True

    # Updates all particles and removes dead ones
    def update(self, delta):
        i = 0

        while i < len(self.active):
            index = self.active[i]
            particle = self.particles[index]

            particle.update(delta)

            dead = particle.age >= particle.lifetime

            if dead:
                self._recycle(i)
                continue

            i += 1

        for emitter in self.emitters:
            emitter.update(delta)

    def _recycle(self, active_index):
        particle_index = self.active[active_index]

        self.particles[particle_index].alive = False

        # Return particle to free the pool
        self.free.append(particle_index)

        last = self.active.pop()

        if active_index < len(self.active):
            self.active[active_index] = last

    # Draws all particles onto the window
    def draw(self, screen):
        screen_width, screen_height = screen.get_size()

        for index in self.active:
            particle = self.particles[index]

            # Particles outside the screen will not be drawn
            if (
                particle.x + particle.width < 0
                or particle.x > screen_width
                or particle.y + particle.height < 0
                or particle.y > screen_height
            ):
                continue

            screen.blit(
                particle.image,
                (int(particle.x), int(particle.y)),
            )

    def create_emitter(
        self,
        *,
        position,
        direction,
        speed: float | tuple[float, float],
        size: float | tuple[float, float],
        lifetime: float = 3.0,
        shape: str = "rect",
        color: str | tuple[int, int, int] | list[tuple[int, int, int]] = "white",
        amount: int = 50,
        burstdelay: float = 0.0,
        spawndelay: float = 0.0,
        spread: float = 0.0,
        gravity: float = 0.0,
    ):
        from .emitter import Emitter

        emitter = Emitter(
            system=self,
            position=position,
            direction=direction,
            speed=speed,
            size=size,
            lifetime=lifetime,
            shape=shape,
            color=color,
            amount=amount if amount <= self.max_particles else self.max_particles,
            burst_delay=burstdelay,
            spawn_delay=spawndelay,
            spread=spread,
            gravity=gravity,
        )

        self.emitters.append(emitter)

        return emitter
