import json
import os
def upjson(bouton_ID='bouton1'):
    filename = 'buttons.json'
    with open(filename, 'r+') as f:
        data = json.load(f)
        data[bouton_ID]['clicks']=data[bouton_ID]['clicks']+1
        print(data)
    os.remove(filename)
    with open(filename, 'w+') as f:
        json.dump(data, f, indent=4)

