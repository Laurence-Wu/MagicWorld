class weapon:
    def __init__(self, name, spell, proficiency):
        self.name = name # the name of the weapon
        self.spell = spell # the spell that can be used by this weapon
        self.proficiency = proficiency # the proficiency of this weapon


class spell:
    def __init__(self, name, power, cost):
        self.name = name # the name of the spell
        self.power = power # the power of the spell
        self.cost = cost # the cost of the spell