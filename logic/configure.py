import json
def config(option, path="config.json"):
    with open(path,'r',encoding='utf-8') as file:
        config = json.load(file)
    return config.get(option)