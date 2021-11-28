import random

class AiCommands:
    # InDir: attack, loot_drops()

    def __init__(self):
        self.loot_table = {
            0: 'Wooden Sword',
            1: '10 Gold'
        }
        self.battle_select = {
            0: 'Slash',
            1: 'Bite'
        }

    def get_loot(self):
        return self.loot_table

    def set_loot(self, loot_table:dict):
        if type(loot_table) != dict:
            raise AttributeError("Please enter dictionary with loot values.")
        self.loot_table = loot_table
        return self.loot_table

    def get_attacks(self):
        return self.battle_select

    def set_attacks(self, attacks:dict):
        self.battle_select = attacks
        return self.battle_select

    def attack(self):
        random_select = random.randint(0, 1)
        return f'Current attack: {self.battle_select[random_select]}!'

    def drop(self):
        random_select = random.randint(0, 1)
        return f'Dropped: {self.loot_table[random_select]}!'    

    def __str__(self):
        return f'Battle Select: {self.battle_select} \n Loot table: {self.loot_table}'