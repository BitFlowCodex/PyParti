import pygame as pg 
import sys
from particle_class import Particle

pg.init()
window = pg.display.set_mode((800,600))
clock = pg.time.Clock()

running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            sys.exit()


    window.fill("black")

    
    pg.display.flip()

    
    clock.tick(60)

pg.quit()

