from pyparti.system import ParticleSystem
from pygame import Surface, Color


def test_spawn():
    system = ParticleSystem(max_particles=10)

    result = system.spawn(
        x=0,
        y=0,
        vx=1,
        vy=1,
        lifetime=5,
        gravity=0,
        shape="circle",
        size=(10, 10),
        color="white",
    )

    assert result is True
    assert len(system.active) == 1
    assert len(system.free) == 9


def test_update_moves_particle():
    system = ParticleSystem(max_particles=10)

    system.spawn(
        x=0,
        y=0,
        vx=10,
        vy=0,
        lifetime=5,
        gravity=0,
        shape="circle",
        size=(10, 10),
        color="white",
    )

    index = system.active[0]
    particle = system.particles[index]

    system.update(1.0)

    assert particle.x == 10
    assert particle.y == 0


def test_update_recycles_dead_particle():
    system = ParticleSystem(max_particles=10)

    system.spawn(
        x=0,
        y=0,
        vx=1,
        vy=0,
        lifetime=1,
        gravity=0,
        shape="circle",
        size=(10, 10),
        color="white",
    )

    assert len(system.active) == 1

    system.update(1.0)

    assert len(system.active) == 0
    assert len(system.free) == 10


def test_recycled_particle_can_be_reused():
    system = ParticleSystem(max_particles=10)

    system.spawn(
        x=0,
        y=0,
        vx=0,
        vy=0,
        lifetime=1,
        gravity=0,
        shape="circle",
        size=(10, 10),
        color="white",
    )

    system.update(1.0)

    result = system.spawn(
        x=100,
        y=100,
        vx=0,
        vy=0,
        lifetime=5,
        gravity=0,
        shape="circle",
        size=(10, 10),
        color="white",
    )

    assert result is True
    assert len(system.active) == 1
    assert len(system.free) == 9

    index = system.active[0]
    particle = system.particles[index]

    assert particle.x == 100
    assert particle.y == 100


def test_get_image_caches_same_image():
    system = ParticleSystem()

    image1 = system._get_image(
        "circle",
        (10, 10),
        "white",
    )

    image2 = system._get_image(
        "circle",
        (10, 10),
        "white",
    )

    assert image1 is image2


def test_draw_is_rendering_the_particle():
    system = ParticleSystem()

    system.spawn(
        x=10,
        y=10,
        vx=0,
        vy=0,
        lifetime=5,
        gravity=0,
        shape="circle",
        size=(10, 10),
        color="white",
    )

    surface = Surface((100, 100))

    system.draw(surface)

    # If the particle is drawn, the pixel at (10, 10) should no longer be transparent
    assert surface.get_at((10, 10)) != Color(0, 0, 0, 0)
