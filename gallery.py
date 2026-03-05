import os
from PIL import Image

def makereadme(history):

    lines=[]

    lines.append("# Autonomous NFT Evolution\n")

    lines.append("## Gallery\n")

    for o in history[-20:]:

        token=o["id"]

        lines.append(f"![{token}](art/{token}.png)\n")

    with open("README.md","w") as f:

        f.write("\n".join(lines))

def makegif():

    os.makedirs("gif",exist_ok=True)

    files=sorted(os.listdir("art"))

    images=[]

    for f in files:

        if f.endswith(".png"):
            images.append(Image.open(f"art/{f}"))

    if len(images)>1:

        images[0].save(
            "gif/evolution.gif",
            save_all=True,
            append_images=images[1:],
            duration=400,
            loop=0
        )
