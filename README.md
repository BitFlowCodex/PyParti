# PyParti

**A fast, beginner-friendly particle system for Pygame.**
Rain, fire, explosions, sparks. Describe an emitter in one call and just simply let the system handle the rest.

| Rain | Explosion | Fire |
|:---:|:---:|:---:|
| <img src="https://github.com/user-attachments/assets/04479380-847e-4283-9f20-75a12faab9b2" width="300"> | <img src="https://github.com/user-attachments/assets/03b816ca-37ba-498b-ba0d-ec5642b52a84" width="300"> | <img src="https://github.com/user-attachments/assets/bf690cae-3685-418b-9af8-8fa65bcd5446" width="300"> |

## Features

- Object pooling and image caching for low per-frame overhead
- Burst or continuous emitters with randomized speed, direction, color, and spread
- Shapes: `rect`, `ellipse`, `circle`
- Optional gravity

## Installation

```bash
pip install git+https://github.com/BitFlowCodex/PyParti.git
```

Requires Python 3.10+ Pygame is installed automatically.

## Usage

```python
import pyparti

system = pyparti.ParticleSystem(max_particles=5000)

system.create_emitter(
    position=(640, 360),
    direction=((-0.1, 0.1), (-10, -9)),
    speed=(25, 50),
    size=15,
    lifetime=4,
    color=[(255, 0, 0), (255, 84, 0)],
    spawndelay=0.05,
    spread=45,
)

# in your game loop
system.update(dt)
system.draw(screen)
```

See [`examples/main.py`](examples/main.py) for rain, fire, and explosion presets.

## Emitter options

Values marked *range* take a number or a `(min, max)` tuple.

| Parameter | Description |
|---|---|
| `position`, `direction` | `(x, y)`, each a *range* |
| `speed`, `size` | *range* |
| `lifetime` | Seconds a particle lives (default `3.0`) |
| `shape` | `"rect"`, `"ellipse"`, or `"circle"` |
| `color` | Name, RGB tuple, or a list to pick from randomly |
| `amount` | Particles per burst (default `50`) |
| `burstdelay` | Seconds between bursts |
| `spawndelay` | Seconds between particles in a stream |
| `spread` | Random angle offset in degrees |
| `gravity` | Downward acceleration in px/s² |

## License

MIT. See [LICENSE](LICENSE).