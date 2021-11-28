import random

class Environment:
    def __init__(self, length=200, width=200):
        self.length = length
        self.width = width
        self.npcs = 1
        self.environment_boost = None

    def get_length(self):
        return self.length

    def set_length(self, length:int):
        self.length = length
        return self.length
    
    def get_width(self):
        return self.width

    def set_width(self, width:int):
        self.width = width
        return self.width

    def get_npcs(self):
        return self.npcs

    def set_npcs(self, value=int):
        self.npcs = value
        return self.npcs

    def get_boost(self):
        return self.environment_boost
    
    def set_boost(self, boost:str):
        self.environment_boost = boost
        return self.environment_boost

class Seed(Environment):
    def __init__(self):
        self.seeded_environment = {
            0: "Volcano",
            1: "Ocean",
            2: "Sky"
        }
        self.length = self.set_length(random.randint(200, 400))
        self.width = self.set_width(random.randint(200, 400))
        self.npcs = self.set_npcs(random.randint(1, 9))

    def __str__(self) -> str:
        return f'Environment: {self.length} by {self.width}, # NPCS: {self.npcs}'