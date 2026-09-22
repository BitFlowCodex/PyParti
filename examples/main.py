import pygame as pg
import sys, pyparti, random

# TODO
# ! Add gravity param for the particle (instead of only boolean)

pg.init()

WIDTH, HEIGHT = 1280, 720

screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()
dt = 0
timer = 0


def checkFPS():
    font = pg.font.Font(None, 64)
    text = font.render(str(int(clock.get_fps())), True, "white")
    textPos = text.get_rect(x=WIDTH / 2, y=10)
    screen.blit(text, textPos)


def explosion():
    return pg.Vector2(random.uniform(-2, 2), random.uniform(-2, 2))


system = pyparti.ParticleSystem()

explosionPar = pyparti.Particle(
    x=WIDTH / 2, y=HEIGHT / 2, size=10, lifeTime=5, delta=dt
)

explosionEm = pyparti.Emitter(
    particleList=system.particles,
    particle=explosionPar,
    amount=20,
    velocity=explosion,
    delay=5.0,
)

running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            sys.exit()

    explosionEm.update(dt)
    system.update()

    screen.fill("black")

    checkFPS()

    system.draw(screen)

    pg.display.flip()

pg.quit()
sys.exit()
