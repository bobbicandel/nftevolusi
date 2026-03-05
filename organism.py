# organism.py

import numpy as np
from PIL import Image
import random

WIDTH = 2048
HEIGHT = 2048


def normalize(v):

    return (v - v.min())/(v.max()-v.min()+1e-9)


def palette(v):

    r = np.sin(v*6.28)*0.5+0.5
    g = np.sin(v*6.28+2)*0.5+0.5
    b = np.sin(v*6.28+4)*0.5+0.5

    rgb = np.stack([r,g,b],axis=-1)

    return (rgb*255).astype(np.uint8)


def generate(seed):

    random.seed(seed)
    np.random.seed(seed)

    xs = np.linspace(-2,2,WIDTH)
    ys = np.linspace(-2,2,HEIGHT)

    x,y = np.meshgrid(xs,ys)

    f = np.sin(x*3)+np.cos(y*3)
    f += np.sin((x*x+y*y)*2)

    f = normalize(f)

    rgb = palette(f)

    img = Image.fromarray(rgb)

    return img
