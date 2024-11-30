import json


class config:
    __config = dict()

    def __init__(self, path="config.json"):
        with open(path, 'r', encoding='utf-8') as file:
            self.__config = json.load(file)

    def get(self, key: str):
        config = self.__config
        for i in key.split('.'):
            config = config.get(i)
        return config
