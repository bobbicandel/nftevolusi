import random
from PIL import Image,ImageDraw
import os

SIZE=2048

def palette(seed):

    random.seed(seed)

    return (
        random.randint(0,255),
        random.randint(0,255),
        random.randint(0,255)
    )

def render(dna,token):

    img=Image.new("RGB",(SIZE,SIZE),(0,0,0))

    draw=ImageDraw.Draw(img)

    base=palette(dna["colorseed"])

    layers=dna["complexity"]//5

    for i in range(layers):

        x=random.randint(0,SIZE)
        y=random.randint(0,SIZE)

        r=random.randint(10,400)

        color=(
            (base[0]+random.randint(-40,40))%255,
            (base[1]+random.randint(-40,40))%255,
            (base[2]+random.randint(-40,40))%255
        )

        if dna["shape"]%2==0:

            draw.ellipse(
                (x-r,y-r,x+r,y+r),
                outline=color,
                width=3
            )

        else:

            draw.rectangle(
                (x-r,y-r,x+r,y+r),
                outline=color,
                width=3
            )

    os.makedirs("art",exist_ok=True)

    path=f"art/{token}.png"

    img.save(path,dpi=(300,300))

    return path
