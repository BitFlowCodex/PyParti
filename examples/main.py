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

# Rain
# system.create_emitter(
#     position=((0, WIDTH), 0),
#     velocity=(0, HEIGHT),
#     lifetime=2,
#     color="blue",
#     amount=200,
#     size=10,
#     delay=0.5,
#     shape="circle",
# )

# Explosion
system.create_emitter(
    position=(WIDTH / 2, HEIGHT / 2),
    velocity=((-100, 100), (-100, 100)),
    speed=50,
    lifetime=1,
    color="red",
    amount=20,
    size=10,
    delay=1,
    shape="rect",
)


running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            sys.exit()

    system.update(dt)

    screen.fill("black")

    checkFPS()

    system.draw(screen)

    pg.display.flip()

pg.quit()
sys.exit()
