
from MagicWorlds.roles import Player, Enemy

class Plotter:
    def __init__(self,Enemies: Enemy):
        self.plot = [] # this is the plot of the story
        self.current_scene = None # this is the current scene of the story
        self.numberOfEnemies = len(Enemies) # this is the number of enemies in the story

    def add_scene(self, scene):
        self.plot.append(scene)

    def next_scene(self):
        # this should be the way to go to the next scene
        pass
    
    def previous_scene(self):
        # this should be the way to go to the previous scene
        pass

class Scene:
    def __init__(self, description):
        self.description = description # this is the description of the scene
        self.actions = [] # this is the list of actions that can be taken in this scene

    def add_action(self, action):
        self.actions.append(action)

    def get_actions(self):
        return self.actions
    




