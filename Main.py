__author__ = "Jarrett Oelmann"


# Command Mage. This program is a text-based adventure
# game. Anything that crashes the program while it runs is considered to be
# the end of the world and is a game over.
# Has Intentional Crashes


def mana():  # function so that I don't have to use the longer print below
    """
    A function to print the world mana variable so that I don't have to copy
    the print statement every time.
    """
    print("The world now has ", world_mana, " mana.",
          sep='')  # the sep='' makes it so that a comma is equal to nothing
    # rather than the default of a space


def combat_obt():
    """
A function to condense code so that I don't have to print multiple times later
    """
    print("1. Attack with fireball")
    print("2. Attack with holy light")
    print("3. Attack with earthquake")
    print("4. Run away")


def surprise_box(num1):  # function with parameter of num1
    """
A function using the input to see if you inputted a 3 or a 7, if you did
input that number then the integer returns 7 to add to world mana
    :param num1: an integer used to see if you guess the right number
    :return: integer to be added to world mana variable
    """
    if num1 == 3 or num1 == 7:  # checks to see if num1 is 3 or 7
        print("You found 7 mana!")
        return 7  # sets the function equal to this amount
    else:
        print("You found nothing in the box")
        return 0


print("Welcome to the world of Command")
print("Will you save this world or be the one to destroy it?")
print("Magic is dangerous to use, a single mistake will destroy this world.")
world_mana = 50  # Sets beginning mana amount
print(world_mana, "mana is left in the world.")
print("You begin your journey to end the lich.")
option_selection = input("You come across a village suffering a drought.\nDo "
                         "you use a rain spell for 10 mana? ")  # asks for an
# input from the user and uses \n in string to make text appear on another
# line.
if option_selection > "x":  # used to check for a yes or no answer by
    # comparing the values of ASCII code of string input
    world_mana -= 10  # subtracts the integer 10 from variable
    # world_mana
    print("You summon rain!",
          end='')  # the end='' makes the next print function display the
    # text on the same line as this print
    print(" drip." * 10)  # repeats the "sound" of rain 10 times on the line
    mana()
    world_mana += 20  # adds the integer 20 to variable world_mana
    print("The world has more mana as a result of your actions!")
    print("The world has ", world_mana, " mana.", sep='')
else:
    print("You ignore" + " the village.")  # the + is used to add the picture
    # of both strings
mana_used = float(input("You continue on and find a huge slime in your "
                        "way!\nHow much mana do you use to try and remove "
                        "it? "))  # asks for an input that comes in as a
# string but is converted to a float
if mana_used >= 3:  # if mana_used is greater than or equal to 3 then...
    world_mana -= mana_used  # subtract the mana_used from
    # world_mana and assign that new value to world_mana
    if world_mana > 0:  # the whole point of this game is to stop world mana
        # from running out so if world_mana is 0 or less it is game over
        print("You removed the slime!")
        mana()
    else:
        print("You caused the world to be destroyed by using the last of its "
              "mana.")
        world_end = 10 % "world"  # Don't know how to end a program so I
        # just crash the code. The code crashing is the end of this world.
else:
    print("You fail to remove the slime!\nYou get absorbed into the "
          "slime!\nThe acid inside slowly dissolves your flesh.\nYou "
          "died.\nThe world follows you just weeks later.")
    world_end = 10 % "world"  # Don't know how to end a program, so I just
    # crash the code. The code crashing is the end of this world.
print("You come across a puzzle door\nThe math puzzle to open the door is (("
      "x^2+1)/5)*1 = 1")
puzzle_input = float(input("How much mana do you push into the door to solve "
                           "the puzzle? "))
world_mana -= puzzle_input
if world_mana > 0:  # if world mana is greater than 0
    mana()
else:
    print(
        "You caused the world to be destroyed by using the last of its mana.")
    world_end = 10 % "world"  # Don't know how to end a program, so I just
    # crash the code. The code crashing is the end of this world.
puzzle_check = (((
                         puzzle_input ** 2) + 1) / 5) * 1  # takes the
# input value assigned to puzzle_input and takes it to the power of 2 and
# then adds a 1 to it, and then it divides by 5 and finally multiplies by 1
# and assigns that to puzzle_check
if puzzle_check == 1:  # checks the variable to see if it is equal to 1
    print("The puzzle door open to a closed room with a single locked chest "
          "inside.")
    mana_used = float(input(
        "How much mana do you use to open the chest? "))  # reassigns the
    # mana_used variable
    world_mana -= mana_used
    if world_mana > 0:
        mana()
    else:
        print("You caused the world to be destroyed by using the last of its "
              "mana.")
        world_end = 10 % "world"  # Don't know how to end a program so I
        # just crash the code. The code crashing is the end of this world.
    puzzle_check = mana_used % 2  # reassigns variable and used to find the
    # remainder of input entered, so I can check for even or odd
    if puzzle_check == 0:  # if variable is a 0 than number inputted is even
        # if there is a one it is odd
        print("The chest opens!\nThere is some mana inside!")
        world_mana += (world_mana // 5)  # take variable and
        # uses floor division by 5 and adds that to world_mana to be
        # assigned to be the new world_mana
        mana()
    else:
        print("You destroy the chest and its contents")
        mana()
    print("You leave the room to continue your quest.")
else:
    print("You could not open the door so you move on.")
print("You run to the next village")
steps = 3
for time in range(1, 4):  # does a for loop and loops 3 times because of range
    print("Arriving in", steps)
    steps -= 1
print("You find a horde of zombies attacking the village")
health = 50
run = 1
while (health >= 0) and (run == 1):  # loops while both conditions are correct
    combat_obt()  # does the defined function
    choice = int(input())
    if choice == 1:  # checks to see if variable is equal to 1
        health -= 11
        world_mana -= 5
        print("You took out a batch.")
    elif choice == 2:
        health -= 26
        world_mana -= 5
        print("You took out a lot of them.")
    elif choice == 3:
        health -= 51
        world_mana -= 30
        print("You took out all of them.")
    elif choice == 4:
        print("You ran away.")
        run = 0
    else:
        print("What did you do?")
    if world_mana > 0:
        mana()
    else:
        print("You caused the world to be destroyed by using the last of its "
              "mana.")
        world_end = 10 % "world"
if run != 0:  # checks to see if variable is not equal to 0
    print("You won and gain 20 mana!")
    world_mana += 20  # adds the right side to variable
    mana()
else:
    print("You ran away and lost 7 mana.")
    world_mana -= 7  # subtracts the right side to variable
    mana()
print("You came across a surprise box, guess the correct number for some "
      "mana!")
guess = int(input("What is your number: "))
world_mana += surprise_box(guess)  # uses variable as argument to function
if not world_mana > 20:  # checks to see if variable is less than 21
    mana()
    print("The gods bless you with more mana")
    world_mana += 10
    mana()
else:
    mana()
    print("You felt someones touch, and no one is nearby.")
print("To be continued")
# I did not use any source beside Pogils and stuff learned in class
