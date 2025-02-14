import json

def open_json(fname ='tiny_Swords.json'):
    f = open(fname, 'r')
    #for line in f.readlines():
    #    print(line.strip())
    tileset = json.load(f)
    f.close()
    return tileset

#open_json('tiny_Swords.json')
tileset = open_json()
print(type(tileset))
for k in tileset:
    print(k)

