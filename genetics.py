import random

def randomdna():
    return {
        "shape": random.randint(0,5),
        "pattern": random.randint(0,5),
        "complexity": random.randint(20,100),
        "symmetry": random.randint(1,6),
        "colorseed": random.randint(0,999999),
        "entropy": random.randint(0,100)
    }

def mutate(dna):

    for k in dna:

        if random.random() < 0.05:

            if isinstance(dna[k],int):
                dna[k]+=random.randint(-5,5)

                if dna[k] < 0:
                    dna[k]=0

    return dna

def inherit(parent):

    dna=dict(parent)

    dna=mutate(dna)

    return dna

def fitness(dna):

    score=0

    score+=dna["complexity"]
    score+=dna["entropy"]
    score+=dna["symmetry"]*5
    score+=random.randint(0,20)

    return score
