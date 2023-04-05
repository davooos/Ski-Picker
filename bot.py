import discord
from discord.ext import commands

token = 'MTA5Mjk2MDc5NzEwMzI0MzI3NA.GaZQab.JeMclvVrSOSXOZgNe-OfL2zgoqiasFKlD02j6w'
intents = discord.Intents.all()
prefix = "/"
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_raw_reaction_add(payload):
    guild = discord.utils.find(lambda g: g.id == payload.guild_id, bot.guilds)
    if payload.emoji.name == 



bot.run(token)

class Skier: # Class for the skier profile, uses total point system to match up with ski
    def __init__(self, name, gender, age, weight, height, skill, region, playfulness, terrain, touring): 
        self.name = name # String with username
        self.gender = gender # String with F or M
        self.age = age # Integer with age
        self.weight = weight # Integer with weight in lbs
        self.height = height # Integer with height in inches
        self.skill = skill # Integer with skill level 1-6
        self.region = region # Integer with region (West, PNW, Rockies, East, Alps)
        self.playfulness = playfulness # Integer with stable being 1 and playful being 6 (1-6)
        self.terrain = terrain # Integer with terrain type (All mountain, all mountain wide, all mountain narrow, powder, carver)
        self.touring = touring # Integer with touring or not

    def get_body_type(self):
        if(self.gender == "M"): # Males
            if(self.weight >= 250 or self.height >= 74):
                return "X" # Very large
            elif(self.weight >= 180 or self.height >= 70):
                return "L" # Large
            elif(self.weight >= 140 or self.height >= 66):
                return "M" # Medium
            elif(self.weight >= 120 or self.height >= 62):
                return "S" # Small
            elif(self.weight < 120 or self.height < 62):
                return "T" # Very small
        if(self.gender == "F"): # Females
            if(self.weight >= 250 or self.height >= 72):
                return "X" # Very large
            elif(self.weight >= 180 or self.height >= 68):
                return "L" # Large
            elif(self.weight >= 120 or self.height >= 64):
                return "M" # Medium
            elif(self.weight >= 100 or self.height >= 60):
                return "S" # Small
            elif(self.weight < 80 or self.height < 55):
                return "T" # Very small

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
        if(self.region == 1):
            return "P" # PNW
        elif(self.region == 2):
            return "W" # West
        elif(self.region == 3):
            return "R" # Rockies
        elif(self.region == 4):
            return "E" # East
        elif(self.region == 5):
            return "A" # Alps
    
    def get_playfulness(self):
        if(self.playfulness == 1):
            return "A" # Most stable
        elif(self.playfulness == 2):
            return "B"
        elif(self.playfulness == 3):
            return "C" 
        elif(self.playfulness == 4):
            return "D" 
        elif(self.playfulness == 5):
            return "E" 
        elif(self.playfulness == 6):
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
        
    def get_touring(self):
        if(self.touring == 1):
            return "Y" # Touring ski
        else:
            return "N" # Otherwise, not touring

def getSkis(file): # Returns list of all the skis
    allSkis = [] # Defines list
    skis = open(file, 'r') # Opens csv file with skis
    for line in skis: # Runs through each line
        line = line.strip() # Strips newline off end 
        allSkis.append(line.split(",")) # Splits up each line by category
    skis.close() # Closes csv file
    allSkis.pop(0) # Removes the headers
    return allSkis

def topThree(skier, skis): # Returns top three ski options
    genderSkis = [] # Defines list for top skis
    topSkis = []

    for ski in skis: # Cycles through each sublist within list
        if(skier.gender == "M"): # Filters out based off gender
            if(ski[2] == "M" or ski[2] == "U"): # If ski is mens or unisex
                genderSkis.append(ski)
        elif(skier.gender == "F"):
            if(ski[2] == "F" or ski[2] == "U"): # If ski is womens or unisex
                genderSkis.append(ski)

    for ski in genderSkis: # Cycles through each sublist within list
        if(skier.get_touring() == "Y"): # Filters out based off touring or not
            if(ski[8] == "Y"): # If ski is touring
                topSkis.append(ski)
        else:
            if(ski[8] == "N"): # If ski is not touring
                topSkis.append(ski)

    bodyType = skier.get_body_type()
    skill = skier.get_skill()
    region = skier.get_region() # Pulls value from each module inside Skier
    playfulness = skier.get_playfulness()
    terrain = skier.get_terrain()

    if(len(topSkis) > 0):
        for ski in topSkis:
            points = 0
            if(bodyType in ski[3]):
                points += 1
            if(skill in ski[4]):
                points += 1
            if(region in ski[5]): # Adds points for each criteria
                points += 1
            if(playfulness in ski[6]):
                points += 1
            if(terrain in ski[7]):
                points += 1
            ski.insert(0, points)
    else:
        return ("No skis found!")
    topSkis.sort(reverse=True) # Sorts list
    output = ("#1: " + topSkis[0][1] + " " + topSkis[0][2] + "\n" + 
              "#2: " + topSkis[1][1] + " " + topSkis[1][2] + "\n" + 
              "#3: " + topSkis[2][1] + " " + topSkis[2][2]) 
    return output

def main():
    name = str(input("What is your username?: "))
    gender = str(input("What is your gender? Enter M or F: "))
    age = int(input("What is your age? Enter a number 1-100: "))
    weight = int(input("What is your weight in lbs? Enter a whole number 1-600: "))
    height = int(input("What is your height in inches? Enter a whole number 1-100: "))
    skill = int(input("What is your skill level? Enter a whole number 1-6, 1 never touched skis, 3 skiing blues, and 6 can ski the entire mountain: "))
    region = int(input("What region do you ski in? Enter 1 for PNW, 2 for US West, 3 for Rockies, 4 for East Cost, and 5 for Alps: "))
    playfulness = int(input("How playful do you want your skis? Enter a number 1-6, 1 being the most stable, 6 being the most playful: "))
    terrain = int(input("What type of ski are you looking for? Enter a number 1-5, 1 being All Mountain, 2 being All Mountain Wide, 3 being All Mountain Narrow, 4 being Powder, and 5 being a Carving Ski: "))
    touring = int(input("Are you looking for a touring ski? Enter 1 for yes, 2 for no: "))
    skier = Skier(name, gender, age, weight, height, skill, region, playfulness, terrain, touring)
    skis = getSkis("SkiList.csv") # Gets list of all skis and information
    print(topThree(skier, skis))

main()
bot.run(token)
