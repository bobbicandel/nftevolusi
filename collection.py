import json
import os

def updatecollection(history):

    os.makedirs("stats",exist_ok=True)

    data=[]

    for o in history:

        data.append({
            "id":o["id"],
            "generation":o["generation"],
            "fitness":o["fitness"],
            "dna":o["dna"],
            "image":f"art/{o['id']}.png",
            "metadata":f"metadata/{o['id']}.json"
        })

    with open("stats/collection.json","w") as f:

        json.dump(data,f,indent=2)
