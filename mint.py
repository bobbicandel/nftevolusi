import json
import os

def traits(dna):

    return [
        {"trait_type":"shape","value":dna["shape"]},
        {"trait_type":"pattern","value":dna["pattern"]},
        {"trait_type":"complexity","value":dna["complexity"]},
        {"trait_type":"symmetry","value":dna["symmetry"]},
        {"trait_type":"entropy","value":dna["entropy"]}
    ]

def mint(token,dna,generation,rarity):

    os.makedirs("metadata",exist_ok=True)

    meta={
        "name":f"Organism {token}",
        "description":"Autonomous evolving organism",
        "image":f"art/{token}.png",
        "dna":dna,
        "generation":generation,
        "rarity":rarity,
        "attributes":traits(dna)
    }

    path=f"metadata/{token}.json"

    with open(path,"w") as f:
        json.dump(meta,f,indent=2)

    return path
