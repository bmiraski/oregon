import random

class Game():
    """Creates a game object to store global game variables """
    def __init__(self):
        self.mileage = 0 # M
        self.south_pass = False # F1
        self.blue_mountains = False # F2
        self.south_pass_mileage = False # M9
        self.cash = 700 # T

class Player():
    """ Creates a player for reference during the game. """
    def __init__(self):
        """ Initializes the specific variables for the player """
        self.injury = False # K8
        self.illness = False #S4
        self.shotskill = 0 # D9
        self.cash = 700 # T

    def __str__(self):
        return "Player Status:: injury: {0}, illness: {1}, shot skill: {2}".format(self.injury, self.illness, self.shotskill)


def print_instructions():
    """ Prints the instructions for the game """
    instructions="""THIS PROGRAM SIMULATES A TRIP OVER THE OREGON TRAIL FROM
    INDEPENDENCE MISSOURI TO OREGON CITY, OREGON IN 1847. YOUR FAMILY OF FIVE
    WILL COVER THE 2040 MILE OREGON TRAIL IN 5-6 MONTHS -- IF YOU MAKE IT
    ALIVE.

    YOU HAD SAVED $900 TO SPEND FOR THE TRIP, AND YOU'VE JUST PAID $200
    FOR A WAGON. YOU WILL NEED TO SPEND THE REST OF YOUR MONEY ON THE FOLLOWING
    ITEMS:

    OXEN: YOU CAN SPEND $200-$300 ON YOUR TEAM. THE MORE YOU SPEND, THE FASTER
    YOU'LL GO BECAUSE YOU'LL HAVE BETTER ANIMALS

    FOOD: THE MORE YOU HAVE, THE LESS CHANCE THERE IS OF GETTING SICK.

    AMMUNITION: $1 BUYS A BELT OF 50 BULLETS. YOU WILL NEED BULLETS FOR ATTACKS
    BY ANIMALS AND BANDITS, AND FOR HUNTING FOOD.

    CLOTHING: THIS IS ESPECIALLY IMPORTANT FOR THE COLD  WEATHER YOU WILL
    ENCOUNTER WHEN CROSSING THE MOUNTAINS.

    MISCELLANEOUS SUPPLIES . THIS INCLUDES MEDICINE AND OTHER THINGS YOU WILL
    NEED FOR SICKNESS AND EMERGENCY REPAIRS.

    YOU CAN SPEND ALL YOUR MONEY BEFORE YOU START YOUR TRIP - OR YOU CAN SAVE
    SOME OF YOUR CASH TO SPEND AT FORTS ALONG THE WAY WHEN YOU RUN LOW. HOWEVER,
    ITEMS COST MORE AT THE FORTS. YOU CAN ALSO GO HUNTING ALONG THE WAY TO GET
    MORE FOOD.

    WHENEVER YOU HAVE TO USE YOUR TRUSTY RIFLE ALONG THE WAY, YOU WILL BE TOLD
    TO TYPE IN A WORD (ONE THAT SOUNDS LIKE A GUN SHOT). THE FASTER YOU TYPE IN
    THAT WORD AND HIT THE **RETURN** KEY, THE BETTER LUCK YOU'LL HAVE WITH YOUR
    GUN.

    AT EACH TURN, ALL ITEMS ARE SHOWN IN DOLLAR AMOUNTS EXCEPT BULLETS

    WHEN ASKED TO ENTER MONEY AMOUNTS, DON'T USE A $.

    GOOD LUCK!!!
    """

    print(instructions)

def shotskill():
    """ Allows the user to choose their rifle skill level. Used for shooting"""
    skill_instructions="""
    How good a shot are you with your rifle?
    1. Ace Marksman
    2. Good shot
    3. Fair to Middlin'
    4. Need more practice
    5. Shaky knees
    Enter the number above. The better you claim you are, the faster you'll have
    to be with your gun to be successful.

    """

    skill = int(input(skill_instructions))
    if skill > 5:
        skill = 0
    return skill

def get_animals():
    animals = int(input("How much do you want to spend on oxen: ")) # A
    return animals

def initial_supplies(game):
    """ Guides user through buying initial supplies """
    budget = game.cash
    spent = 0
    animals = 0
    while animals < 200 OR animals >= 300:
        print("You must spend between 200 and 300 on oxen.")
        animals = get_animals()


def main():
    needinstructions = input("Do you need instructions? (Yes / No) ")
    if needinstructions[:1].lower() == "y":
        print_instructions()

    game = Game()
    player = Player()
    player.shotskill = shotskill()
    initial_supplies(game)

    print(player)

    fort_option = -1 # X1
    turn = 0 # D3




main()
