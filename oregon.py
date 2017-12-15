import random


class Game():
    """Creates a game object to store global game variables """
    def __init__(self):
        self.mileage = 0  # M
        self.mileage2 = 0  # M2
        self.south_pass = False  # F1
        self.blue_mountains = False  # F2
        self.south_pass_mileage = False  # M9
        self.cash = 700  # T
        self.animals = 0  # A
        self.food = 0  # F
        self.bullets = 0  # B
        self.clothing = 0  # C
        self.misc = 0  # M1
        self.fort_option = False  # X1
        self.blizzard = False  # L1
        self.poor_clothing = False  # C1

    def __str__(self):
        return (f"""
                Game Status::
                mileage: {self.mileage},
                south_pass: {self.south_pass},
                blue_mountains: {self.blue_mountains},
                south_pass_mileage: {self.south_pass_mileage},
                cash: {self.cash},
                animals: {self.animals},
                food: {self.food},
                bullets: {self.bullets},
                clothing: {self.clothing},
                misc: {self.misc}
                """.lstrip())


class Player():
    """ Creates a player for reference during the game. """
    def __init__(self):
        """ Initializes the specific variables for the player """
        self.injury = False  # K8
        self.illness = False  # S4
        self.shotskill = 0  # D9

    def __str__(self):
        return (f"""
               Player Status::
               injury: {self.injury},
               illness: {self.illness},
               shot skill: {self.shotskill}
               """.lstrip())


def shotskill():
    """ Allows the user to choose their rifle skill level. Used for shooting"""
    skill_instructions = """
    How good a shot are you with your rifle?
    1. Ace Marksman
    2. Good shot
    3. Fair to Middlin'
    4. Need more practice
    5. Shaky knees
    Enter the number above. The better you claim you are, the faster you'll
    have to be with your gun to be successful.

    """

    skill = int(input(skill_instructions))
    if skill > 5:
        skill = 0
    return skill


def initial_supplies(game):
    """ Guides user through buying initial supplies """
    budget = game.cash
    animals = 0
    while (animals < 200 or animals >= 300):
        print("You must spend between 200 and 300 on oxen.")
        animals = int(input("How much do you want to spend on oxen: "))  # A
    game.animals = animals
    budget = budget - animals

    food = 0
    print("You have ", budget, " remaining to spend on supplies.")
    while (food <= 0 or food > budget):
        food = int(input("How much would you like to spend on food: "))  # F
    game.food = food
    budget = budget - food
    print("You have ", budget, " remaining to spend on supplies.")

    bullets = int(
        input("How much would you like to spend on ammunition: ")
        )  # B
    while (bullets < 0 or bullets > budget):
        print("That is impossible.")
        bullets = int(
            input("How much would you like to spend on ammunition: ")
            )
    budget = budget - bullets
    game.bullets = bullets * 50
    print("You have ", budget, " remaining to spend on supplies.")

    clothing = int(
        input("How much would you like to spend on clothing: ")
        )  # C
    while (clothing < 0 or clothing > budget):
        print("That is impossible.")
        clothing = int(input("How much would you like to spend on clothing: "))
    game.clothing = clothing
    budget = budget - clothing
    print("You have ", budget, " remaining to spend on supplies.")

    misc = int(input("How much would like to spend on misc. supplies: "))  # M1
    while (misc < 0 or misc > budget):
        print("That is impossible.")
        misc = int(input("How much would like to spend on misc. supplies: "))
    game.misc = misc
    game.cash = budget - misc
    print("After all your purchases, you now have", game.cash, "dollars left.")


def print_date(turn):
    """ Prints the date that corresponds to the turn """
    dates = [0, "April 12", "April 26", "May 10", "May 24", "June 7",
             "June 21", "July 5", "July 19", "August 2", "August 16",
             "August 31", "September 13", "September 27", "October 11",
             "October 25", "November 8", "November 22", "December 6",
             "December 20"]
    print("Monday,", dates[turn]+",", "1847")


def visit_doctor(game, player):
    """ Handles the visit to the doctor when player is injured or sick."""
    game.cash -= 20
    if game.cash >= 0:
        print("Doctor's bill is $20.")
    else:
        game.cash = 0
        print("You can't afford a doctor.")
        process_death(player)


def process_fort_menu(game, player):
    """Processes the game turns with a fort option in the menu"""
    menu = """
           Do you want to:
           (1) Stop at the next fort
           (2) Hunt
           (3) Continue
           """
    choice = int(input(menu))
    if choice == 1:
        fort_shopping(game, player)
        return
    elif choice == 2:
        hunting(game, player)
        return
    else:
        return


def process_no_fort_menu(game, player):
    """Processes the game turns with no fort optiion in the menu"""
    menu = """
           Do you want to:
           (1) Hunt
           (2) Continue
           """
    choice = int(input(menu))
    if choice == 1:
        hunting(game, player)
        return
    else:
        return


def eating(game):
    """Processes eating each turn"""
    menu = """
           Do you want to eat:
           (1) Poorly
           (2) Moderately
           (3) Well
           """
    while (choice < 1 or choice > 3):
        choice = int(input(menu))
    food = game.food - (5*choice) - 8
    if food <= 0:
        print("You can't eat that well!")
        eating(game)
    game.food = food
    return


def process_death(player):
    """Determines how player dies"""
    diseases = ["dysentery", "pneumonia", "black fever", "small pox",
                "cholera", "the shakes", "yellow fever", "dysentery",
                "dysentery", "dysentery"]

    if player.injury:
        print("You died of injuries!")
    else:
        rdm = random.Random()
        disease_idx = rdm.randint(1, 10) - 1
        disease_death = "You have died of {0}.".format(diseases[disease_idx])
        print(disease_death)
    death()


def run_turn(game, player):
    rdm = random.Random()

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

    if (player.illness or player.injury):
        visit_doctor(game, player)

    if game.south_pass_mileage:
        print("Total mileage is 950.")
    else:
        print(f"Total mileage is {game.mileage}.")

    game.south_pass_mileage = False

    print(f"""Food: {game.food}, Bullets: {game.bullets},
              Clothing: {game.clothing}, Misc. Supplies: {game.misc},
              Cash: {game.cash}""")

    if game.fort_option:
        process_fort_menu(game, player)
    else:
        process_no_fort_menu(game, player)

    game.fort_option = not game.fort_option

    if game.food < 13:
        print("You ran out of food and died.")
        death()

    eating(game)

    game.mileage = (game.mileage
                    + 200
                    + (game.animals - 220) / 5
                    + 10 * rdm.random()
                    )
    game.blizzard = False
    game.poor_clothing = False

    rider_check = (((game.mileage/100 - 4)**2 + 72
                    / (game.mileage/100 - 4)**2 + 12)
                   - 1
                   )
    if (rdm.random() * 10) < rider_check:
        riders_attack(game, player)

    

def death():
    """This does nothing at the moment but will handle the death sequence"""
    print("PLACEHOLDER: You are dead.")


def main():
    needinstructions = input("Do you need instructions? (Yes / No) ")
    if needinstructions.lower().startswith('y'):
        with open('instructions.txt') as instructions:
            print(instructions.read())

    game = Game()
    player = Player()
    turn = 0  # D3
    player.shotskill = shotskill()
    initial_supplies(game)

    print(player)
    print(game)

    turn += 1
    if turn <= 19:
        print_date(turn)
    else:
        print("""You have been on the trail too long. Your family dies in the
                 the first blizzard of winter""")
        death()

    run_turn(game, player)


main()
