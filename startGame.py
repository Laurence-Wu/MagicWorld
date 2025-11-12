# this will start the game

from MagicWorlds.gameEngine import Plotter
from MagicWorlds.roles import Enemies, Heros


user = Heros()
enemies = []
for i in range(3): # for testing reasons, I just set the number of enemies to 3
    enemy = Enemies()
    enemies.append(enemy)
plotter = Plotter(enemies)

while(user.health > 0 and enemy):
    user_action = input("What do you want to do?")
    if user_action == "attack":
        user.attack(enemy)
    elif user_action == "defend":
        user.defend()
    elif user_action == "cast spell":
        user.cast_spell()
    elif user_action == "run away":
        user.run_away()
    else:
        print("Invalid action.")