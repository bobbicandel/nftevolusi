import json
import os
from collections import Counter

def calculaterarity(history):

    traits=[]

    for o in history:
        traits.append(o["dna"]["shape"])
        traits.append(o["dna"]["pattern"])

    freq=Counter(traits)

    rarity={}

    for k,v in freq.items():

        rarity[k]=1/v

    os.makedirs("stats",exist_ok=True)

    with open("stats/rarity.json","w") as f:

        json.dump(rarity,f,indent=2)

    return rarity
