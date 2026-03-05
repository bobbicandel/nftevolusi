import random
import math
import os
from PIL import Image, ImageDraw

SIZE = 2048
CENTER = SIZE // 2


def palette(seed):

    random.seed(seed)

    palettes = [

        [(255,90,90),(255,200,120),(255,255,200)],
        [(90,200,255),(120,255,200),(200,255,255)],
        [(200,120,255),(120,90,255),(255,200,255)],
        [(120,255,120),(200,255,120),(255,255,200)],
        [(255,120,200),(255,200,255),(200,120,255)]

    ]

    return random.choice(palettes)


def radial_point(angle, radius):

    x = CENTER + math.cos(angle) * radius
    y = CENTER + math.sin(angle) * radius

    return (x, y)


def branch(draw, angle, dna, colors):

    steps = dna["complexity"] // 2

    entropy = dna["entropy"] / 100

    radius = 10

    prev = (CENTER, CENTER)

    for i in range(steps):

        radius += random.uniform(10, 40)

        angle += random.uniform(-entropy, entropy)

        p = radial_point(angle, radius)

        color = random.choice(colors)

        width = random.randint(2,6)

        draw.line([prev, p], fill=color, width=width)

        if random.random() < 0.25:

            r = random.randint(4,12)

            draw.ellipse(
                (p[0]-r,p[1]-r,p[0]+r,p[1]+r),
                fill=color
            )

        prev = p


def ring(draw, dna, colors):

    nodes = dna["complexity"] // 3

    radius = random.randint(200,800)

    for i in range(nodes):

        angle = random.random() * math.pi * 2

        p = radial_point(angle, radius)

        r = random.randint(5,15)

        draw.ellipse(
            (p[0]-r,p[1]-r,p[0]+r,p[1]+r),
            fill=random.choice(colors)
        )


def render(dna, token):

    img = Image.new("RGB",(SIZE,SIZE),(8,8,12))

    draw = ImageDraw.Draw(img)

    colors = palette(dna["colorseed"])

    symmetry = max(3, dna["symmetry"] * 2)

    for arm in range(symmetry):

        angle = (math.pi * 2 / symmetry) * arm

        branch(draw, angle, dna, colors)

    for i in range(3):

        ring(draw, dna, colors)

    glow = Image.new("RGB",(SIZE,SIZE),(0,0,0))
    gdraw = ImageDraw.Draw(glow)

    for i in range(200):

        x = random.randint(0,SIZE)
        y = random.randint(0,SIZE)

        r = random.randint(1,3)

        gdraw.ellipse(
            (x-r,y-r,x+r,y+r),
            fill=random.choice(colors)
        )

    img = Image.blend(img, glow, 0.15)

    os.makedirs("art", exist_ok=True)

    path = f"art/{token}.png"

    img.save(path, dpi=(300,300))

    return path
