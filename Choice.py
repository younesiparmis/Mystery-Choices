import sys
import random
import time

# ---------------------------
# Utility functions
# ---------------------------
def slow_print(text, delay=0.03):
    """Print text slowly for better storytelling."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def choose_option(options):
    """Display options and get a valid input from the player."""
    while True:
        for i, option in enumerate(options, 1):
            print("{}. {}".format(i, option))
        choice = input("Enter your choice (1-{}): ".format(len(options)))
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        else:
            print("Invalid choice! Try again.\n")

# ---------------------------
# Game paths
# ---------------------------
score = 0

def start_adventure():
    global score
    slow_print("✨ Welcome to the Magical Kingdom, dear adventurer! ✨\n")
    slow_print("You wake up in a mystical garden. Paths lie ahead of you.\n")
    
    options = ["Go towards the sparkling tree", 
               "Walk by the shimmering river", 
               "Sit on the colorful flowers and relax"]
    choice = choose_option(options)
    
    if choice == 1:
        tree_path()
    elif choice == 2:
        river_path()
    elif choice == 3:
        flower_path()

def tree_path():
    global score
    slow_print("\n🌳 You reach a sparkling tree with a mysterious glowing box beneath it.\n")
    options = ["Open the box", "Leave it alone"]
    choice = choose_option(options)
    
    if choice == 1:
        score += 10
        slow_print("\n💫 A fairy appears and grants you magical powers! You feel stronger!")
        score += random.randint(5, 15)
        slow_print("Your score increased! Current score: {}\n".format(score))
        dragon_path()
    else:
        score -= 5
        slow_print("\n💨 The box releases pink clouds and you cough! You decide to leave quickly.")
        slow_print("Your score decreased! Current score: {}\n".format(score))
        river_path()

def river_path():
    global score
    slow_print("\n🏞️ You arrive at the shimmering river. A magical boat is waiting.\n")
    options = ["Ride the boat", "Walk along the riverbank"]
    choice = choose_option(options)
    
    if choice == 1:
        score += 10
        slow_print("\n⛵ The boat takes you to a hidden island full of treasures!")
        treasure_path()
    else:
        score += 5
        slow_print("\n💎 You find a sparkling gem on the riverbank!")
        slow_print("Your score increased! Current score: {}\n".format(score))
        tree_path()

def flower_path():
    global score
    slow_print("\n🌸 You sit among the flowers and hear a soft, magical melody.\n")
    options = ["Follow the sound", "Take a nap"]
    choice = choose_option(options)
    
    if choice == 1:
        score += 10
        slow_print("\n🧚 You meet a fairy who invites you to a magical tea party!")
        tea_party()
    else:
        score += 5
        slow_print("\n💤 You dream of flying with butterflies! It's wonderful!")
        slow_print("Your score increased! Current score: {}\n".format(score))
        dragon_path()

def dragon_path():
    global score
    slow_print("\n🐉 Suddenly, a friendly dragon appears in your path!")
    options = ["Ride the dragon", "Hide behind a bush"]
    choice = choose_option(options)
    
    if choice == 1:
        score += 20
        slow_print("\n🔥 You soar through the skies with the dragon! Amazing adventure!")
        slow_print("Final score: {}\n".format(score))
        end_game("victory")
    else:
        score -= 10
        slow_print("\n🌿 The dragon notices you and blows smoke. You escape safely but lost points.")
        slow_print("Final score: {}\n".format(score))
        end_game("safe_escape")

def treasure_path():
    global score
    slow_print("\n💰 On the island, you find three treasure chests.")
    options = ["Open the golden chest", "Open the silver chest", "Open the bronze chest"]
    choice = choose_option(options)
    
    if choice == 1:
        score += 30
        slow_print("\n✨ The golden chest has a magical crown! You are now royalty!")
        end_game("royal")
    elif choice == 2:
        score += 15
        slow_print("\n💎 The silver chest has precious gems. Wealthy adventurer!")
        end_game("rich")
    else:
        score += 5
        slow_print("\n🍫 The bronze chest has candies and chocolate! Sweet adventure!")
        end_game("sweet")

def tea_party():
    global score
    slow_print("\n🍵 The tea party has three treats: cake, potion, and fruit.")
    options = ["Eat the cake", "Drink the potion", "Pick fruit"]
    choice = choose_option(options)
    
    if choice == 1:
        score += 10
        slow_print("\n🎂 Delicious cake! You feel happy and energized!")
    elif choice == 2:
        score += 20
        slow_print("\n✨ The potion grants you temporary magical powers!")
    else:
        score += 5
        slow_print("\n🍎 Fruit is refreshing! You feel calm and joyful!")
    
    slow_print("Your score increased! Current score: {}\n".format(score))
    dragon_path()

# ---------------------------
# End game
# ---------------------------
def end_game(outcome):
    slow_print("\n🏁 Adventure Over!")
    if outcome == "victory":
        slow_print("Congratulations! You had an epic dragon adventure!")
    elif outcome == "safe_escape":
        slow_print("You survived the dragon encounter safely. Good job!")
    elif outcome == "royal":
        slow_print("You became royalty! Your magical adventure ends happily!")
    elif outcome == "rich":
        slow_print("Rich with gems and treasures! Amazing!")
    elif outcome == "sweet":
        slow_print("Sweet treats for a sweet adventurer!")
    else:
        slow_print("Thanks for playing!")
    
    slow_print("Final Score: {}\n".format(score))
    sys.exit()

# ---------------------------
# Start the game
# ---------------------------
start_adventure()
