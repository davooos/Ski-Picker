class Skier: # Class for the skier profile, uses total point system to match up with ski
    def __init__(self, name, gender, age, weight, height, skill, region, playfulness, terrain): 
        self.name = name # String with username
        self.gender = gender # String with F or M
        self.age = age # Integer with age
        self.weight = weight # Integer with weight in lbs
        self.height = height # Integer with height in ft
        self.skill = skill # Integer with skill level 1-6
        self.region = region # String with region (West, PNW, Rockies, East, Alps)
        self.playfullness = playfulness # Integer with stable being 1 and playful being 6 (1-6)
        self.terrain = terrain # String with terrain type (All mountain, all mountain wide, all mountain narrow, powder, carver)

    def get_body_type(self):
        pass
