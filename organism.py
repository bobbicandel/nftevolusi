# organism.py
# Ultra Sharp Neon Evolution Engine
# GitHub Actions friendly (no terminal needed)

import numpy as np
from PIL import Image
import random
import os
import json

WIDTH = 2048
HEIGHT = 2048

HISTORY_FILE = "history.json"
ART_DIR = "art"

os.makedirs(ART_DIR, exist_ok=True)


def get_generation():
    if not os.path.exists(HISTORY_FILE):
        history = {"generation": 0}
    else:
        with open(HISTORY_FILE) as f:
            history = json.load(f)

    history["generation"] += 1

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

    return history["generation"]


def normalize(v):
    return (v - v.min()) / (v.max() - v.min() + 1e-9)


def neon_palette(v):

    r = np.sin(v * 6.28) * 0.5 + 0.5
    g = np.sin(v * 6.28 + 2.1) * 0.5 + 0.5
    b = np.sin(v * 6.28 + 4.2) * 0.5 + 0.5

    rgb = np.stack([r, g, b], axis=-1)
    rgb = np.power(rgb, 0.6)

    return (rgb * 255).astype(np.uint8)


def fractal_field(x, y):

    value = np.zeros_like(x)

    freq = 1.0
    amp = 1.0

    for _ in range(5):
        value += amp * np.sin(x * freq + np.cos(y * freq))
        value += amp * np.cos(y * freq + np.sin(x * freq))

        freq *= 1.9
        amp *= 0.5

    return value


def crystal_field(x, y):

    r = np.sqrt(x*x + y*y)
    a = np.arctan2(y, x)

    spikes = np.sin(a * 12)
    radial = np.cos(r * 10)

    return spikes * radial


def generate_image(seed):

    random.seed(seed)
    np.random.seed(seed)

    xs = np.linspace(-2, 2, WIDTH)
    ys = np.linspace(-2, 2, HEIGHT)

    x, y = np.meshgrid(xs, ys)

    field1 = fractal_field(x, y)
    field2 = crystal_field(x, y)

    combined = normalize(field1 + field2)

    rgb = neon_palette(combined)

    img = Image.fromarray(rgb)

    return img


def main():

    generation = get_generation()

    seed = random.randint(0, 999999)

    img = generate_image(seed)

    path = f"{ART_DIR}/{generation}.png"

    img.save(path, "PNG")

    print("generated", path)


if __name__ == "__main__":
    main()
