import pygame as pg 
import sys
from particle_class import *

pg.init()
window = pg.display.set_mode((800,600))
clock = pg.time.Clock()
running: bool = True

# Particle system instance
system = ParticleSystem()

# Shows FPS counter on screen (optional)
def checkFPS():
    font = pg.font.Font(None, 64)
    text = font.render(str(int(clock.get_fps())), True, "white")
    textPos = text.get_rect(x=window.get_width()/ 2,y=10)
    window.blit(text, textPos)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            sys.exit()
    
    # Mouse state and position
    mouse = pg.mouse.get_pressed()[0]
    mPos = pg.mouse.get_pos()
    
    # Spawn particles when the left mouse is held
    if mouse:
        system.emit(mPos[0], mPos[1], 5, size=20, color="white", duration=5, is_gravity=False)
    
    # Update all active particles
    system.update()
        
    window.fill("black")
    
    # Draw all particles
    system.draw(window)
    
    pg.display.flip()
    
    clock.tick(60)

pg.quit()
