from src.character.defaults import Character
from src.environment.room_seed import Seed
from src.commands.ai_commands import AiCommands
from src.commands.player_commands import PlayerCommands

plyr1 = Character()
print("Player", plyr1)
plyr1_commands = PlayerCommands()
print(plyr1_commands)

npc1 = Character('Slime', 10, 1, 5, 0)
print("NPC", npc1)
npc1_commands = AiCommands()
print(npc1_commands)

npc2 = Character('Boss')
print("NPC", npc2)

room1 = Seed()
print(room1)

room2 = Seed()
print(room2)