import os
import random
import math
from PIL import Image, ImageDraw, ImageFilter

SIZE = 2048
CENTER = SIZE // 2


def palette(seed):

    random.seed(seed)

    palettes = [

        [(0,255,255),(0,180,255),(0,120,255)],
        [(255,0,200),(255,80,255),(255,0,120)],
        [(0,255,120),(120,255,180),(0,255,200)],
        [(255,120,0),(255,200,0),(255,80,40)],
        [(120,0,255),(200,120,255),(160,80,255)]

    ]

    return random.choice(palettes)


def radial(angle, r):

    x = CENTER + math.cos(angle) * r
    y = CENTER + math.sin(angle) * r

    return (x, y)


def background(draw):

    for i in range(1200):

        x = random.randint(0, SIZE)
        y = random.randint(0, SIZE)

        g = random.randint(10,30)

        draw.point((x,y),(g,g,g))


def energyfield(img, colors):

    glow = Image.new("RGB",(SIZE,SIZE),(0,0,0))
    draw = ImageDraw.Draw(glow)

    for i in range(200):

        x = random.randint(0,SIZE)
        y = random.randint(0,SIZE)

        r = random.randint(40,200)

        draw.ellipse(
            (x-r,y-r,x+r,y+r),
            fill=random.choice(colors)
        )

    glow = glow.filter(ImageFilter.GaussianBlur(120))

    return Image.blend(img, glow, 0.35)


def fractalbranches(draw, dna, colors):

    arms = max(4, dna["symmetry"] * 3)

    steps = dna["complexity"] // 2

    entropy = dna["entropy"] / 100

    for a in range(arms):

        angle = (math.pi*2/arms)*a

        x,y = CENTER,CENTER

        radius = 10

        for i in range(steps):

            radius += random.uniform(10,40)

            angle += random.uniform(-entropy, entropy)

            nx,ny = radial(angle,radius)

            color = random.choice(colors)

            w = random.randint(2,6)

            draw.line((x,y,nx,ny),fill=color,width=w)

            if random.random() < 0.25:

                r = random.randint(6,16)

                draw.ellipse(
                    (nx-r,ny-r,nx+r,ny+r),
                    fill=color
                )

            x,y = nx,ny


def liquidmetal(draw, dna):

    rings = dna["symmetry"] * 4

    for i in range(rings):

        r = random.randint(200,900)

        shade = random.randint(140,220)

        color = (shade,shade,shade)

        w = random.randint(2,8)

        draw.ellipse(
            (CENTER-r,CENTER-r,CENTER+r,CENTER+r),
            outline=color,
            width=w
        )


def plasmablobs(draw, dna, colors):

    blobs = dna["complexity"]

    for i in range(blobs):

        angle = random.random()*math.pi*2

        dist = random.uniform(0,SIZE*0.35)

        x,y = radial(angle,dist)

        r = random.randint(60,220)

        draw.ellipse(
            (x-r,y-r,x+r,y+r),
            fill=random.choice(colors)
        )


def particles(draw, colors):

    for i in range(2000):

        x = random.randint(0,SIZE)
        y = random.randint(0,SIZE)

        draw.point((x,y), random.choice(colors))


def liquiddistort(img, dna):

    px = img.load()

    strength = dna["entropy"] // 3

    for i in range(50000):

        x = random.randint(1,SIZE-2)
        y = random.randint(1,SIZE-2)

        dx = random.randint(-strength,strength)
        dy = random.randint(-strength,strength)

        try:
            px[x,y] = px[x+dx,y+dy]
        except:
            pass

    return img


def render(dna, token):

    img = Image.new("RGB",(SIZE,SIZE),(6,6,12))

    draw = ImageDraw.Draw(img)

    colors = palette(dna["colorseed"])

    background(draw)

    plasmablobs(draw, dna, colors)

    fractalbranches(draw, dna, colors)

    liquidmetal(draw, dna)

    particles(draw, colors)

    img = img.filter(ImageFilter.GaussianBlur(20))

    img = energyfield(img, colors)

    img = liquiddistort(img, dna)

    img = img.filter(ImageFilter.SMOOTH_MORE)

    os.makedirs("art",exist_ok=True)

    path = f"art/{token}.png"

    img.save(path,dpi=(300,300))

    return path
