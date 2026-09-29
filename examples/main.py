import pygame as pg
import sys, pyparti, random

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


def rain():
    system.create_emitter(
        position=((0, WIDTH), 0),
        direction=(0, HEIGHT),
        speed=200,
        lifetime=10,
        color=[
            (0, 169, 255),
            (3, 96, 179),
            (0, 131, 255),
        ],
        amount=200,
        size=15,
        shape="ellipse",
    )


def explosion():
    system.create_emitter(
        position=(WIDTH / 2, HEIGHT / 2),
        direction=((0, 1), (4.5, 5)),
        speed=(50, 500),
        lifetime=1,
        color=[
            (255, 0, 0),
            (255, 84, 0),
            (255, 34, 0),
        ],
        amount=100,
        size=15,
        burstdelay=1,
        shape="rect",
        spread=180,
    )


def fire():
    system.create_emitter(
        position=(WIDTH / 2, HEIGHT / 2),
        direction=((0, 1), (4.5, 5)),
        speed=(50, 100),
        lifetime=1.5,
        color=[
            (255, 0, 0),
            (255, 84, 0),
            (255, 34, 0),
        ],
        amount=100,
        size=15,
        burstdelay=1.5,
        shape="rect",
        spread=180,
    )


rain()


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
