import discord
import time
from discord.ext import commands

class Skier: # Class for the skier profile, uses total point system to match up with ski
    def __init__(self, name, gender, weight, height, skill, region, playfulness, terrain, touring): 
        self.name = name # String with username
        self.gender = gender # String with F or M
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
    skill = skier.skill()
    region = skier.region() # Pulls value from each module inside Skier
    playfulness = skier.playfulness()
    terrain = skier.terrain()

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

#--------------------------------------------Discord Bot-----------------------------------------------------#

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(bot.user.name + " ready")

@bot.command()
async def start(ctx):
    name = ctx.author.name # Gets username of user
    print(name + " is using the bot")
    await ctx.send(embed=discord.Embed(title="Hello " + name + "!", description="Please wait for the reactions to fully add before reacting.\nCreated by davooos#7792"))
    time.sleep(2)

    genderInput = await ctx.send(embed=discord.Embed(description="What is your gender? Select M or F.")) # Asks user for gender
    while True: # Loops until either male or female selected
        await genderInput.add_reaction("\U0001f1f2") # male
        await genderInput.add_reaction("\U0001f1eb") # female
        gender, user = await bot.wait_for('reaction_add') # emoji value
        if(str(gender) == "\U0001f1eb"): # If user selects female
            gender = "F"
            break
        elif(str(gender) == "\U0001f1f2"): # If user selects male
            gender = "M"
            break
        genderInput = await ctx.send(embed=discord.Embed(description="\u26A0\uFE0F Please react with one of the options!")) # Prompts user to react again if they send invalid reaction

    await ctx.send(embed=discord.Embed(description="What is your weight in lbs? Type in a whole number 60-600!")) # WEIGHT
    while True: # Loops until valid weight inputted
        weightInput = await bot.wait_for('message')
        weight = weightInput.content # Raw weight value
        if(weight.isdigit()): # Checks if weight is an integer
            weight = int(weight) # Changes weight to integer from string
            if(weight <= 600 and weight >= 60): # Checks if weight is in range
                break # Breaks out of while loop
        await ctx.send(embed=discord.Embed(description="\u26A0\uFE0F Please enter a valid whole number 60-600!")) # Prompts user again for weight

    await ctx.send(embed=discord.Embed(description="What is your height in inches? Type in a whole number 48-90!")) # HEIGHT
    while True: # Loops until valid height inputted
        heightInput = await bot.wait_for('message')
        height = heightInput.content # Raw height value
        if(height.isdigit()): # Checks if weight is an integer
            height = int(height) # Changes height to integer from string
            if(height <= 90 and height >= 48): # Checks if height is in range
                break # Breaks out of while loop
        await ctx.send(embed=discord.Embed(description="\u26A0\uFE0F Please enter a valid whole number 48-90!")) # Prompts user again for height

    skillInput = await ctx.send(embed=discord.Embed(description="What is your skill level? Choose a number 1-6\n1: Brand New\n2: Greens\n3: Blues\n4: Blacks \n5: Double Blacks\n6: All Terrain")) # SKILL LEVEL
    while True: # Loops until 1-6 selected
        await skillInput.add_reaction("1\uFE0F\u20E3") # 1
        await skillInput.add_reaction("2\uFE0F\u20E3") # 2
        await skillInput.add_reaction("3\uFE0F\u20E3") # 3
        await skillInput.add_reaction("4\uFE0F\u20E3") # 4
        await skillInput.add_reaction("5\uFE0F\u20E3") # 5
        await skillInput.add_reaction("6\uFE0F\u20E3") # 6
        skill, user = await bot.wait_for('reaction_add') # waits for reaction
        if(str(skill) == "1\uFE0F\u20E3"):
            skill = "F"
            break
        elif(str(skill) == "2\uFE0F\u20E3"):
            skill = "G"
            break
        elif(str(skill) == "3\uFE0F\u20E3"):
            skill = "B"
            break
        elif(str(skill) == "4\uFE0F\u20E3"):
            skill = "L"
            break
        elif(str(skill) == "5\uFE0F\u20E3"):
            skill = "D"
            break
        elif(str(skill) == "6\uFE0F\u20E3"):
            skill = "A"
            break
        skillInput = await ctx.send("\u26A0\uFE0F Please react with one of the options!") # Prompts user again for skill

    regionInput = await ctx.send(embed=discord.Embed(description="Where do you normally ski? Choose a location\n\U0001f327\uFE0F: Pacific Northwest\n\U0001f332: Western US\n\U0001faa8: Rockies\n\U0001f9ca: East Coast\n\U0001f3d4\uFE0F: Alps")) # REGION 
    while True: # Loops until 1-6 selected
        await regionInput.add_reaction("\U0001f327\uFE0F") # PNW
        await regionInput.add_reaction("\U0001f332") # West
        await regionInput.add_reaction("\U0001faa8") # Rockies
        await regionInput.add_reaction("\U0001f9ca") # East
        await regionInput.add_reaction("\U0001f3d4\uFE0F") # Alps
        region, user = await bot.wait_for('reaction_add') # waits for reaction
        if(str(region) == "\U0001f327\uFE0F"):
            region = "P"
            break
        elif(str(region) == "\U0001f332"):
            region = "W"
            break
        elif(str(region) == "\U0001faa8"):
            region = "R"
            break
        elif(str(region) == "\U0001f9ca"):
            region = "E"
            break
        elif(str(region) == "\U0001f3d4\uFE0F"):
            region = "A"
            break
        regionInput = await ctx.send(embed=discord.Embed(description="\u26A0\uFE0F Please react with one of the options!")) # Prompts user again for region 

    playfulnessInput = await ctx.send(embed=discord.Embed(description="How playful or stiff do you want your ski? Choose a number 1-6\n(1 being most stable, 6 being most playful)")) # PLAYFUL LEVEL
    while True: # Loops until 1-6 selected
        await playfulnessInput.add_reaction("1\uFE0F\u20E3") # Stiff
        await playfulnessInput.add_reaction("2\uFE0F\u20E3") 
        await playfulnessInput.add_reaction("3\uFE0F\u20E3") 
        await playfulnessInput.add_reaction("4\uFE0F\u20E3") 
        await playfulnessInput.add_reaction("5\uFE0F\u20E3") 
        await playfulnessInput.add_reaction("6\uFE0F\u20E3") # Playful
        playfulness, user = await bot.wait_for('reaction_add') # waits for reaction
        if(str(playfulness) == "1\uFE0F\u20E3"):
            playfulness = "F"
            break
        elif(str(playfulness) == "2\uFE0F\u20E3"):
            playfulness = "G"
            break
        elif(str(playfulness) == "3\uFE0F\u20E3"):
            playfulness = "B"
            break
        elif(str(playfulness) == "4\uFE0F\u20E3"):
            playfulness = "L"
            break
        elif(str(playfulness) == "5\uFE0F\u20E3"):
            playfulness = "D"
            break
        elif(str(playfulness) == "6\uFE0F\u20E3"):
            playfulness = "A"
            break
        playfulnessInput = await ctx.send(embed=discord.Embed(description="\u26A0\uFE0F Please react with one of the options!")) # Prompts user again for skill

    terrainInput = await ctx.send(embed=discord.Embed(description="What type of ski are you looking for? Choose an option\n\U0001f3bf: All Mountain\n\U0001f53c: All Mountain Wide\n\U0001f53d: All Mountain Narrow\n\u2744\uFE0F: Powder\n\U0001f90f: Carver")) # TERRAIN 
    while True: # Loops until 1-6 selected
        await terrainInput.add_reaction("\U0001f3bf") # AM a
        await terrainInput.add_reaction("\U0001f53c") # AMW
        await terrainInput.add_reaction("\U0001f53d") # AMN
        await terrainInput.add_reaction("\u2744\uFE0F") # Pow a
        await terrainInput.add_reaction("\U0001f90f") # Carver a
        terrain, user = await bot.wait_for('reaction_add') # waits for reaction
        if(str(terrain) == "\U0001f3bf"):
            terrain = "A" # All mountain
            break
        elif(str(terrain) == "\U0001f53c"):
            terrain = "W" # AM Wide
            break
        elif(str(terrain) == "\U0001f53d"):
            terrain = "N" # AM Narrow
            break
        elif(str(terrain) == "\u2744\uFE0F"):
            terrain = "P" # Powder
            break
        elif(str(terrain) == "\U0001f90f"):
            terrain = "C" # Carver
            break
        terrainInput = await ctx.send(embed=discord.Embed(description="\u26A0\uFE0F Please react with one of the options!")) # Prompts user again for region 

    touringInput = await ctx.send(embed=discord.Embed(description="Are you looking for a touring ski?\nSelect Y for yes N for no")) # TOURING
    while True:
        await touringInput.add_reaction("")
        await touringInput.add_reaction("")
        touring, user = await bot.wait_for('reaction_add')
        if(str(touring) == ""):
            touring = "Y"
            break
        elif(str(touring) == ""):
            touring = "N"
            break
    touringInput = await ctx.send(embed=discord.Embed(description="\u26A0\uFE0F Please react with one of the options!"))

    skier = Skier(name, gender, weight, height, skill, region, playfulness, terrain, touring)
    skis = getSkis("SkiList.csv") # Gets list of all skis and information
    await ctx.send(embed=discord.Embed(description=topThree(skier, skis)))


token = open("token.txt", "r").read()
bot.run(token)
bot.run(token)

# TO-DO: Finish discord.py integration