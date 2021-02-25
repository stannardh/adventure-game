from random import randint
import pycodestyle
import random
import time

items = []
fairies_spells = ["mushroom", "toad", "lobster", "balloon", "chair", "carrot"]
damage = randint(12, 123)
body = ["ear", "nose", "cheek", "chin", "butt", "arm", "leg"]
action = ["scratches", "hits", "pokes", "licks", "punches"]
emotion = ["anger", "frustration",
           "fury", "irritation", "desperation", "rage", "wrath", "impotence"]


def print_pause(message_to_print, pause=2):
    print(message_to_print)
    time.sleep(pause)


def intro():
    print_pause(
        "You find yourself standing in an open field,"
        " filled with grass and yellow wildflowers.")
    print_pause(
        "Rumour has it that a wicked fairie is somewhere around here, "
        "and has been terrifying the nearby village...")


def invalid_move():
    print_pause("I'm sorry, this isn't a valid move. Please try again")


def choose_location():
    print_pause("Where would you like to go?\n"
                "Please enter the location you would like to visit:")
    location = input("Where would you like to go?\n"
                     "1. The House \n"
                     "2. The Cave \n"
                     "3. The Forest \n").lower()
    if "house" in location:
        house()
    elif "cave" in location:
        cave()
    elif "forest" in location:
        forest()
    else:
        invalid_move()
        choose_location()


def game_over():
    print_pause("GAME OVER")
    play_again = input("Would you like to play again? \n"
                       "Press Y or N \n").upper()
    if play_again == "Y":
        play_game()
        global items
        items = []
    elif play_again == "N":
        print_pause("Thank you for playing")
    else:
        invalid_move()
        game_over()


def house():
    if "fairie" in items:
        print_pause(
            "With the feisty fairie cursing at you from your bag, "
            "you head back to the house, hoping the wizard can help.")
        print_pause(
            "You knock again and wait a few seconds"
            " when the door creaks open by itself.")
        print_pause("Cautiously you make your way inside\n"
                    "The wizard is sitting by the fire smoking a pipe\n")
        print_pause("Walking up to him, you tap him on the shoulder")
        print_pause("He turns his head...")
        print_pause("You *GASP*! He has no face!")
        print_pause("You stumble backwards and hit your head on the table")
        print_pause("and everything", 1)
        print_pause("goes", 1)
        print_pause("BLACK", 1)
        print_pause("You wake up some time later and realise,"
                    " it was all a dream \n"
                    "YOU WIN!")
        game_over()
    elif "torch" in items:
        house_list = ['the wizard scowls at you, points to somewhere behind '
                      'you and slams the door.',
                      'a cat jumps out from under the table and runs '
                      'out of the door between your legs',
                      'you flip the switch to turn on the lights, '
                      'but nothing happens']
        house_action = random.choice(house_list)
        print_pause(house_action)
        print_pause("There's nothing more here")
        print_pause("You go back to the field")
        choose_location()
    else:
        print_pause("You knock on the door of the house...")
        print_pause("...the door opens...")
        print_pause("a wizard greets you and asks your name")
        name = input("Hello, what is your name? ")
        print_pause(
            f"Nice to meet you {name} but there's nothing for you here, "
            "the forest is nice for visitors.")
        print_pause(
            "You turn away from the door and notice "
            "a torch on the ground beside you. "
            "You bend down to pick it up.  You go back to the field.", 3)
        items.append("torch")
        choose_location()


def cave():
    print_pause(
        "You walk towards the entrance of the cave...")
    print_pause("You peer into the mouth of the cave")
    if "torch" and "net" in items:
        print_pause(
            "A bear has made its home in the cave, and snarls at you. "
            "You can't go back in")
        choose_location()
    elif "torch" in items:
        print_pause("You enter the cave")
        print_pause("You switch on the torch and the cave comes ALIVE!")
        print_pause(
            "You jump back in fear as a huge cloud of swirling claws"
            " come towards you screeching in anger", 3)
        print_pause("But WAIT!...", 1)
        print_pause(
            "It's not a cloud of claws, it's a family of bats"
            " that woke up when you turned on the torch")
        print_pause(
            "Then you notice, there on the roof,"
            " where the bats were sleeping...")
        print_pause(
            "A glittering silver net, with rubies encrusted in the hilt,"
            " hangs from the ceiling."
            "  You pick it up and go back to the field.")
        items.append("net")
        choose_location()
    else:
        print_pause("You enter the cave")
        print_pause(
            "It's too dark to see, you need to find something to help."
            "  You go back to the field.")
        choose_location()


def forest():
    if "fairie" in items:
        print_pause(
            "The leprachaun has gathered troops of centaurs,"
            " unicorns and werewolves, they turn you away"
            " and won't let you back in.")
        choose_location()
    elif "torch" in items:
        print_pause("A thick forest lies in front of you \n"
                    "The trees stand like a sentry against invaders")
        print_pause("You approach the thick trees")
        print_pause("SNAP! \n"
                    "You turn around quickly"
                    " to see what caused the noise but see nothing")
        print_pause("You continue on...")
        print_pause("SNAP \n"
                    "There it is again!")
        print_pause(
            "You jump as you see a leprachaun sitting on a"
            " branch ahead of you, snapping twigs and humming softly")
        print_pause(
            "You ask him if he has heard about the fairie"
            " that has been troubling the town")
        print_pause("He looks at you sadly\n"
                    "Shakes his head\n"
                    "And points towards a small clearing to the west")
        print_pause(
            "You head towards the clearing and hear a blood curdling shriek")
        print_pause("It's the fairie! She's here!\n"
                    "Do you choose to fight her or run?\n"
                    "Please enter what you wish to do. \n")
        response = input("Fight or Run?\n").lower()
        if "fight" in response:
            fight()
        elif "run" in response:
            print_pause("You choose to run!\n")
            print_pause(
                "Ducking under a branch and letting a twig ping behind you,"
                " in hopes of hitting the fairie,"
                " you run as fast as you can", 3)
            print_pause(
                "You can hear the beating of her wings close behind"
                " and the sound of her raspy cackle as she closes in on you")
            print_pause("She's getting closer!")
            print_pause(
                f"The fairie swoops down and {random.choice(action)}"
                f" on the {random.choice(body)}"
                f" and deals you {damage} of damage")
            print_pause("The fairie tries again!\n"
                        f"The fairie bites you on the {random.choice(body)}..."
                        f" you turn into a {random.choice(fairies_spells)}")
            print_pause("YOU LOSE!")
            game_over()
    else:
        print_pause(
            "it's too dark to see anything...."
            " come back if you find something to help")
        choose_location()


def fight():

    print_pause(
        "You chose to fight! "
        f"The fairie swoops towards you in {random.choice(emotion)},"
        " beating her wings ferociously and gnashing her teeny,"
        " tiny teeth!", 3)
    print_pause(
        f"The fairie misses but {random.choice(action)}"
        f" you on the {random.choice(body)}"
        f" and deals you {damage} of damage!")
    if "net" in items:
        print_pause("You swing the net wildly in front of you and miss!")
        print_pause(
            f"The fairie {random.choice(action)} you"
            f" on the {random.choice(body)}"
            f" and deals you {damage} of damage!", 3)
        print_pause(
            f"Brandishing the net in {random.choice(emotion)},"
            f" you hear a sudden SHRIEK of {random.choice(emotion)}"
            " as the fairie gets stuck in the net.")
        print_pause(
            "Wiping the sweat from your brow, you look down at the tiny thing,"
            " barely bigger that a butterfly...")
        print_pause("How could something so tiny, cause so much chaos?")
        print_pause("What should you do with it now?")
        print_pause(
            "Securing the fairie carefully in your bag,"
            " you make your way back to the house,"
            " the wizard will know what to do.")
        items.append("fairie")
        choose_location()
    else:
        print_pause("You have nothing to help you catch her!")
        print_pause(
            "You try to use the torch to hit her but she's too fast!")
        print_pause(
            f"The fairie {random.choice(action)} you"
            f" on the {random.choice(body)} and deals you {damage} of damage!")
        print_pause(
            "You wait until she's so close that you can feel the air"
            " from her tiny wings against your face")
        print_pause("You swing the torch...", 1)
        print_pause(
            f"The fairie {random.choice(action)} you"
            f" on the {random.choice(body)} and deals you {damage} of damage!")
        print_pause("You miss!")
        print_pause(
            f"The fairie bites you on the {random.choice(body)}..."
            f" you turn into a {random.choice(fairies_spells)}")
        print_pause("YOU LOSE!")
        game_over()


def play_game():
    intro()
    choose_location()


if __name__ == '__main__':
    play_game()
