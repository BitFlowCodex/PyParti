from pyparti.emitter import Emitter
from pyparti.system import ParticleSystem
from math import sqrt, isclose


def test_normalize_pair():
    assert Emitter._normalize_pair(10) == (10, 10)
    assert Emitter._normalize_pair((5, 10)) == (5, 10)


def test_normalize_range():
    result = Emitter._normalize_range(
        (
            (10, 20),
            (30, 40),
        )
    )

    assert result == ((10, 20), (30, 40))


def test_normalize_colors():
    assert Emitter._normalize_colors("yellow") == ["yellow"]
    assert Emitter._normalize_colors((255, 255, 255)) == [(255, 255, 255)]
    assert Emitter._normalize_colors(["red", "green", "blue"]) == [
        "red",
        "green",
        "blue",
    ]


def test_random_position():
    system = ParticleSystem()

    emitter = Emitter(
        system=system,
        position=((10, 20), (30, 40)),
        direction=((-1, 1), (-1, 1)),
        speed=(5, 10),
        size=(10, 20),
        lifetime=5,
        shape="circle",
        color="white",
        amount=10,
        burst_delay=0,
        spawn_delay=0,
        spread=10,
        gravity=0,
    )

    result = emitter._random_position()

    assert 10 <= result[0] <= 20
    assert 30 <= result[1] <= 40


def test_random_direction():
    system = ParticleSystem()

    emitter = Emitter(
        system=system,
        position=((10, 20), (30, 40)),
        direction=((-1, 1), (-1, 1)),
        speed=(5, 10),
        size=(10, 20),
        lifetime=5,
        shape="circle",
        color="white",
        amount=10,
        burst_delay=0,
        spawn_delay=0,
        spread=10,
        gravity=0,
    )

    result = emitter._random_direction()

    length = sqrt(result[0] ** 2 + result[1] ** 2)

    assert isclose(length, 1.0)


def test_emit_spawns_particles():
    system = ParticleSystem()

    emitter = system.create_emitter(
        position=((0, 0), (0, 0)),
        direction=((1, 1), (0, 0)),
        speed=10,
        size=10,
        amount=3,
    )

    emitter.emit()

    # check if active contains them now
    assert len(system.active) == 3


def test_emitter_update_spawns_particles():
    system = ParticleSystem()

    emitter = system.create_emitter(
        position=((0, 0), (0, 0)),
        direction=((1, 1), (0, 0)),
        speed=10,
        size=10,
        amount=1,
        spawndelay=1.0,
    )

    emitter.update(1.0)

    assert len(system.active) == 1
