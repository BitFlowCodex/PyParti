import pygame as pg 
import sys, random
from particle_class import Particle

pg.init()
window = pg.display.set_mode((800,600))
clock = pg.time.Clock()
running: bool = True


particles: list = []


while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            sys.exit()
    
    mouse = pg.mouse.get_pos()
    if pg.mouse.get_pressed()[0]:
        particles.append(Particle(mouse[0],mouse[1], 10.0, random.choice(["red","orange"]) , 10))

    window.fill("black")
    for particle in particles:
        if particle.is_alive():
            particle.draw(window)
        particle.update()
 
    pg.display.flip()
    
    clock.tick(60)

pg.quit()
