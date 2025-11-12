


# Alright, here's the prompt engine for this fucking magic world!
# the math tools that we are using are differential geometry / information theory(game theory) / signal processing / modern control theory / graph theory / random processes

class Heros:
    def __init__(self, name, age, occupation, interests):
        self.name = input("please input your desired name") # this is the name of the user
        self.weapon = input("please input your desired weapon") # this is the weapon of the user, it should be one of the following: the math tools that we are using are differential geometry / information theory(game theory) / signal processing / modern control theory / graph theory / random processes
        self.interests = input("please input your desired interests") # this is the interests of the user
        self.proficiency = 100 # for this proficiency, it should be determined with the self.interests, but for testing reasons, I just set it to 100
        self.spell = [] # the name of the spell that can be used by the user with the weapon.
        self.health = 100 # the health of the user

class Enemies:
    def __init__(self, name, age, occupation, interests):
        self.problem =  input("input the problem that you want to solve")
        self.name = "Dark Lord" # you should load a small model to determine the name of this enemy.

    def attack(self):
        pass
        # this should be the way to attack the user
        # you should input the user's solution to the initial problem, and then evaluate the ratio of advantage to disadvantage, and deal with a certain amound of damage to the user.
