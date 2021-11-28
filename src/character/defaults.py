class Character():
    def __init__(self, name=None, hp=100, base_stat=10, accuracy=70, block=10):
        self.name = name
        self.hp = hp
        self.base_stat = base_stat
        self.accuracy = accuracy
        self.block = block

    def get_hp(self):
        return self.hp
    
    def set_hp(self, value:int):
        self.hp = value
        return self.hp

    def get_stats(self):
        return self.base_stat

    def set_stats(self, value:int):
        self.base_stat = value
        return self.base_stat

    def get_accuracy(self):
        return self.accuracy

    def set_accuracy(self, value:int):
        self.accuracy = value
        return self.accuracy

    def get_block(self):
        return self.block

    def set_block(self, value:int):
        self.block = value
        return self.block

    def get_name(self):
        return self.name

    def set_name(self, name:str):
        self.name = name
        return self.name

    def __str__(self):
        return f'{self.name} Stats | HP: {self.hp}, Base Stats: {self.base_stat}, Accuracy: {self.accuracy}, Block Chance: {self.block}'