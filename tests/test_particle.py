from pyparti.particle import Particle
from pygame import Surface


def test_particle_update():
    image = Surface((10, 10))

    p = Particle()
    p.reset(
        x=0,
        y=0,
        vx=10,
        vy=0,
        lifetime=5,
        gravity=10,
        image=image,
    )

    p.update(1.0)

    assert p.x == 10
    assert p.y == 10
    assert p.vy == 10


def test_particle_is_reseted():
    particle = Particle()
    image = Surface((10, 20))

    particle.reset(
        x=100,
        y=100,
        vx=5,
        vy=10,
        lifetime=3,
        gravity=9.8,
        image=image,
    )

    assert particle.x == 100
    assert particle.y == 100
    assert particle.vx == 5
    assert particle.vy == 10
    assert particle.lifetime == 3
    assert particle.gravity == 9.8
    assert particle.image == image
