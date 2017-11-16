import random

class Game():
    """Creates a game object to store global game variables """
    def __init__(self):
        self.mileage = 0 # M
        self.mileage2 = 0 # M2
        self.south_pass = False # F1
        self.blue_mountains = False # F2
        self.south_pass_mileage = False # M9
        self.cash = 700 # T
        self.animals = 0 # A
        self.food = 0 # F
        self.bullets = 0 # B
        self.clothing = 0 # C
        self.misc = 0 # M1


    def __str__(self):
        return """Game Status:: mileage: {0}, south_pass: {1}, blue_mountains:
                {2}, south_pass_mileage: {3}, cash: {4}, animals: {5},
                food: {6}, bullets: {7}, clothing: {8}, misc: {9}""".format(
                self.mileage,self.south_pass, self.blue_mountains,
                self.south_pass_mileage,self.cash, self.animals, self.food,
                self.bullets, self.clothing, self.misc)


class Player():
    """ Creates a player for reference during the game. """
    def __init__(self):
        """ Initializes the specific variables for the player """
        self.injury = False # K8
        self.illness = False #S4
        self.shotskill = 0 # D9


    def __str__(self):
        return """Player Status:: injury: {0}, illness: {1},
        shot skill: {2}""".format(self.injury, self.illness, self.shotskill)


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


def initial_supplies(game):
    """ Guides user through buying initial supplies """
    budget = game.cash
    spent = 0
    animals = 0
    while (animals < 200 or animals >= 300):
        print("You must spend between 200 and 300 on oxen.")
        animals = int(input("How much do you want to spend on oxen: ")) # A
    game.animals = animals
    budget = budget - animals

    food = 0
    print("You have ", budget, " remaining to spend on supplies.")
    while (food <= 0 or food > budget):
        food = int(input("How much would you like to spend on food: ")) # F
    game.food = food
    budget = budget - food
    print("You have ", budget, " remaining to spend on supplies.")

    bullets = int(input("How much would you like to spend on ammunition: ")) #B
    while (bullets < 0 or bullets > budget):
        print("That is impossible.")
        bullets = int(input("How much would you like to spend on ammunition: "))
    budget = budget - bullets
    game.bullets = bullets * 50
    print("You have ", budget, " remaining to spend on supplies.")

    clothing = int(input("How much would you like to spend on clothing: ")) # C
    while (clothing < 0 or clothing > budget):
        print("That is impossible.")
        clothing = int(input("How much would you like to spend on clothing: "))
    game.clothing = clothing
    budget = budget - clothing
    print("You have ", budget, " remaining to spend on supplies.")

    misc = int(input("How much would like to spend on misc. supplies: ")) #M1
    while (misc < 0 or misc > budget):
        print("That is impossible.")
        misc = int(input("How much would like to spend on misc. supplies: "))
    game.misc = misc
    game.cash = budget - misc
    print("After all your purchases, you now have ",game.cash," dollars left.")


def print_date(turn):
    """ Prints the date that corresponds to the turn """
    dates=[0,"April 12", "April 26", "May 10", "May 24", "June 7", "June 21",
           "July 5", "July 19", "August 2", "August 16", "August 31",
           "September 13", "September 27", "October 11", "October 25",
           "November 8", "November 22", "December 6", "December 20"]
    print("Monday, ", dates[turn], ", 1847")

def visit_doctor(game, player):
    """ Handles the visit to the doctor when player is injured or sick."""
    game.cash =- 20
    if game.cash >= 0:
        print("Doctor's bill is $20.")
    else:
        game.cash = 0
        print("You can't afford a doctor.")
        process_death(player)


def process_death(player):
    """Determines how player dies"""
    diseases = ["dysentery", "pneumonia", "black fever", "small pox", "cholera",
    "the shakes", "yellow fever", "dysentery", "dysentery", "dysentery"]

    if player.injury = 1:
        print("You died of injuries!")
    else:
        rdm = random.Random()
        disease_idx = rdm.randint(1,10) - 1
        disease_death = "You have died of {0}.".format(diseases[disease_idx])
        print(disease_death)
    death()

def run_turn(game, player):
    if game.food < 0:
        game.food = 0
    else:
        game.food = int(game.food)

    if game.bullets < 0:
        game.bullets = 0
    else:
        game.bullets = int(game.bullets)

    if game.clothing < 0:
        game.clothing = 0
    else:
        game.clothing = int(game.clothing)

    if game.misc < 0:
        game.misc = 0
    else:
        game.misc = int(game.misc)

    if game.food < 13:
        print("You'd better do some hunting or buy food and soon!")

    game.mileage2 = game.mileage

    if (game.illness == 1 or game.injury == 1):
        visit_doctor(game, player)





def death():
    """This does nothing at the moment but will handle the death sequence"""
    print("PLACEHOLDER: You are dead.")

def main():
    needinstructions = input("Do you need instructions? (Yes / No) ")
    if needinstructions[:1].lower() == "y":
        print_instructions()

    game = Game()
    player = Player()
    turn = 0 # D3
    player.shotskill = shotskill()
    initial_supplies(game)

    print(player)
    print(game)

    fort_option = -1 # X1

    turn =+ 1
    if turn <=19:
        print_date(turn)
    else:
        print("""You have been on the trail too long. Your family dies in the
                 the first blizzard of winter""")
        death()

    run_turn(game, player)







main()
