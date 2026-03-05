import json
import os
import random

import genetics
import organism
import mint
import rarity
import collection
import gallery

POP=5

def loadhistory():

    if not os.path.exists("history.json"):

        return {"generation":0,"supply":0,"organisms":[]}

    with open("history.json") as f:

        return json.load(f)

def savehistory(h):

    with open("history.json","w") as f:

        json.dump(h,f,indent=2)

def evolve():

    history=loadhistory()

    gen=history["generation"]+1

    organisms=history["organisms"]

    new=[]

    parents=organisms[-POP:]

    for i in range(POP):

        if parents:

            p=random.choice(parents)["dna"]

            dna=genetics.inherit(p)

        else:

            dna=genetics.randomdna()

        fitness=genetics.fitness(dna)

        token=history["supply"]+1

        path=organism.render(dna,token)

        rarityscore=random.random()

        mint.mint(token,dna,gen,rarityscore)

        o={
            "id":token,
            "generation":gen,
            "dna":dna,
            "fitness":fitness
        }

        new.append(o)

        history["supply"]+=1

    organisms.extend(new)

    organisms=sorted(organisms,key=lambda x:x["fitness"],reverse=True)

    organisms=organisms[:100]

    history["organisms"]=organisms

    history["generation"]=gen

    savehistory(history)

    rarity.calculaterarity(organisms)

    collection.updatecollection(organisms)

    gallery.makereadme(organisms)

    gallery.makegif()

if __name__=="__main__":

    evolve()
