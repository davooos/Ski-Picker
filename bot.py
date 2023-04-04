class Skier: # Class for the skier profile, uses total point system to match up with ski
    def __init__(self, name, gender, age, weight, height, skill, region, playfulness, terrain, touring): 
        self.name = name # String with username
        self.gender = gender # String with F or M
        self.age = age # Integer with age
        self.weight = weight # Integer with weight in lbs
        self.height = height # Integer with height in ft
        self.skill = skill # Integer with skill level 1-6
        self.region = region # Integer with region (West, PNW, Rockies, East, Alps)
        self.playfullness = playfulness # Integer with stable being 1 and playful being 6 (1-6)
        self.terrain = terrain # Integer with terrain type (All mountain, all mountain wide, all mountain narrow, powder, carver)
        self.touring = touring # Integer with touring or not

    def get_body_type(self):
        pass

    def get_skill(self): # Returns skill level with letter
        if(self.skill == 1):
            return "F" # First timer
        elif(self.skill == 2):
            return "G" # Greens
        elif(self.skill == 3):
            return "B" # Blues
        elif(self.skill == 4):
            return "L" # Blacks
        elif(self.skill == 5):
            return "D" # Double blacks
        elif(self.skill == 6):
            return "A" # All terrain
    
    def get_region(self): # Returns region with letter
        if(self.region == "1"):
            return "P" # PNW
        elif(self.region == "2"):
            return "W" # West
        elif(self.region == "3"):
            return "R" # Rockies
        elif(self.region == "4"):
            return "E" # East
        elif(self.region == "5"):
            return "A" # Alps
    
    def get_playfulness(self):
        if(self.playfullness == 1):
            return "A" # Most stable
        elif(self.playfullness == 2):
            return "B"
        elif(self.playfullness == 3):
            return "C" 
        elif(self.playfullness == 4):
            return "D" 
        elif(self.playfullness == 5):
            return "E" 
        elif(self.playfullness == 6):
            return "F" # Most playful

    def get_terrain(self):
        if(self.terrain == 1):
            return "A" # All mountain
        elif(self.terrain == 2):
            return "W" # All mntn wide
        elif(self.terrain == 3):
            return "N" # All mntn narrow
        elif(self.terrain == 4):
            return "P" # Powder
        elif(self.terrain == 5):
            return "C" # Carver

