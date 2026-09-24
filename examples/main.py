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


system = pyparti.ParticleSystem()


def explosion():
    particle = pyparti.Particle(
        position=pg.Vector2(WIDTH / 2, HEIGHT / 2),
        velocityRange=((-10, 40), (0, 75)),
        size=(10, 10),
        lifeTime=1,
        shape="circle",
     
    )

    emitter = pyparti.Emitter(
        particleList=system.particles,
        particle=particle,
        amount=50,
        delay=0.2,
    )

    return emitter


exp = explosion()

running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            sys.exit()

    exp.update(dt)
    system.update(dt)

    screen.fill("black")

    checkFPS()

    system.draw(screen)

    pg.display.flip()

pg.quit()
sys.exit()
