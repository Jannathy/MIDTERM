# Declare these variables at the top so that they are globally accessible
inventory = []  # A list that stores items the player picks up
health = 100  # The player's health

def get_user_info():
    print("========================================")
    print("         Welcome to Your Adventure!")
    print("========================================\n")

    name = input("Enter your name: ").strip()
    while not name:
        print("Name cannot be empty. Please try again.")
        name = input("Enter your name: ").strip()

    age = input("Enter your age: ").strip()
    while not age.isdigit():
        print("Please enter a valid age.")
        age = input("Enter your age: ").strip()

    print(f"\nHi, {name}! Let's begin your adventure!! :D\n")

    return name, age

def start_adventure(player_name):
    print("=============================================")
    print("        Journey to Find the Lost Relic")
    print("=============================================\n")
    print("Introduction:")
    print(f"{player_name}, you are an adventurer seeking the legendary lost relic, rumored to grant immense power.")
    print("Your journey begins at the edge of the Darkwood Forest, where many have ventured but few returned.")
    print("Prepare yourself for a perilous journey filled with choices that will determine your fate.\n")
    enchanted_forest(player_name)

def enchanted_forest(player_name):
    print("You step into the Darkwood Forest. The canopy is thick, blocking most of the sunlight.")
    print("Ahead, you see two paths:")
    print("1. A narrow trail leading deeper into the forest.")
    print("2. A wider path that seems to follow a river.")
    print("\nYour choices: [narrow] or [wide]")
    choice = input("> ").lower()

    if choice == 'narrow':
        narrow_trail(player_name)
    elif choice == 'wide':
        wide_path(player_name)
    else:
        print("Invalid response, respond with one of the choices in the brackets\n")
        enchanted_forest(player_name)

def narrow_trail(player_name):
    print("\nYou take the narrow trail. The forest becomes denser, and the sounds of wildlife grow louder.")
    print("After walking for a while, you encounter a fork in the path:")
    print("1. Take the [left] path towards the sound of running water.")
    print("2. Take the [right] path where the trees are twisted and ominous.")
    choice = input("> ").lower()

    if choice == 'left':
        river_bank(player_name)
    elif choice == 'right':
        dark_clearing(player_name)
    else:
        print("Invalid response, respond with one of the choices in the brackets\n")
        narrow_trail(player_name)

def wide_path(player_name):
    print("\nYou follow the wide path along the river. The sound of flowing water is soothing.")
    print("Soon, you come across an old fisherman who offers to help you.")
    print("1. [Accept] the fisherman's help.")
    print("2. [Decline] the offer and continue alone.")
    choice = input("> ").lower()

    if choice == 'accept':
        fisherman_help(player_name)
    elif choice == 'decline':
        solo_continue(player_name)
    else:
        print("Invalid response, respond with one of the choices in the brackets\n")
        wide_path(player_name)

def river_bank(player_name):
    print("\nYou follow the sound of running water to a serene riverbank.")
    print("There is a small boat and a rickety bridge crossing the river.")
    print("1. Use the [boat] to cross the river.")
    print("2. Attempt to cross the [bridge].")
    choice = input("> ").lower()

    if choice == 'boat':
        boat_crossing(player_name)
    elif choice == 'bridge':
        bridge_crossing(player_name)
    else:
        print("Invalid response, respond with one of the choices in the brackets\n")
        river_bank(player_name)

def dark_clearing(player_name):
    print("\nYou take the right path into the twisted trees and arrive at a dark clearing.")
    print("A wild wolf blocks your path.")
    print("1. Try to [befriend] the wolf.")
    print("2. Attempt to [fight] the wolf.")
    choice = input("> ").lower()

    if choice == 'befriend':
        befriend_wolf(player_name)
    elif choice == 'fight':
        fight_wolf(player_name)
    else:
        print("Invalid response, respond with one of the choices in the brackets\n")
        dark_clearing(player_name)

def fisherman_help(player_name):
    print("\nThe fisherman shares valuable information about the Lost Relic's location.")
    print("He offers you a magical amulet for protection.")
    print("1. [Take] the amulet.")
    print("2. [Decline] the amulet.")
    choice = input("> ").lower()

    if choice == 'take':
        print("You received the amulet. It might prove useful later.")
        inventory.append('amulet')
        hidden_path(player_name)
    elif choice == 'decline':
        print("You continue your journey without the amulet.")
        hidden_path(player_name)
    else:
        print("Invalid response, respond with one of the choices in the brackets\n")
        fisherman_help(player_name)

def solo_continue(player_name):
    print("\nYou decide to continue alone, relying solely on your skills.")
    print("After hours of trekking, you find an abandoned campsite.")
    print("1. [Investigate] the camp for useful items.")
    print("2. [Keep moving] to avoid potential dangers.")
    choice = input("> ").lower()

    if choice == 'investigate':
        print("You find a healing potion. This will help if you encounter danger.")
        inventory.append('healing potion')
        hidden_path(player_name)
    elif choice == 'keep moving':
        hidden_path(player_name)
    else:
        print("Invalid response, respond with one of the choices in the brackets\n")
        solo_continue(player_name)

def boat_crossing(player_name):
    print("\nYou board the boat and start crossing the river.")
    if 'amulet' in inventory:
        print("The amulet glows, protecting you from the river's magical currents.")
        print("You safely reach the other side.")
        hidden_path(player_name)
    else:
        print("Without protection, the river's magic overwhelms you.")
        print("You are swept away by the currents.")
        game_over(player_name)

def bridge_crossing(player_name):
    print("\nYou attempt to cross the rickety bridge.")
    print("The bridge starts to collapse!")
    print("1. [Run] across.")
    print("2. [Jump] back to safety.")
    choice = input("> ").lower()

    if choice == 'run':
        print("You sprint across the bridge just in time.")
        hidden_path(player_name)
    elif choice == 'jump':
        print("You jump back safely but the bridge collapses behind you.")
        hidden_path(player_name)
    else:
        print("Invalid response, respond with one of the choices in the brackets\n")
        bridge_crossing(player_name)

def befriend_wolf(player_name):
    print("\nYou try to befriend the wolf by offering some of your food.")
    if 'food' in inventory:
        print("The wolf accepts your offer and becomes your companion.")
        inventory.append('wolf companion')
        hidden_path(player_name)
    else:
        print("You have no food to offer. The wolf attacks you.")
        game_over(player_name)

def fight_wolf(player_name):
    print("\nYou decide to fight the wolf.")
    print("Do you use your [sword] or [magic]?")
    choice = input("> ").lower()

    if choice == 'sword':
        if 'sword' in inventory:
            print("With your sword, you slay the wolf.")
            print("However, you sustain injuries.")
            global health
            health -= 30
            if health > 0:
                hidden_path(player_name)
            else:
                game_over(player_name)
        else:
            print("You have no sword to fight with. The wolf overpowers you.")
            game_over(player_name)
    elif choice == 'magic':
        if 'amulet' in inventory:
            print("You use the amulet's magic to defeat the wolf effortlessly.")
            hidden_path(player_name)
        else:
            print("You have no magical items. The wolf overpowers you.")
            game_over(player_name)
    else:
        print("Invalid response, respond with one of the choices in the brackets\n")
        fight_wolf(player_name)

def hidden_path(player_name):
    print("\nContinuing your journey, you discover a hidden path leading to a cave entrance.")
    print("1. Enter the [cave].")
    print("2. Bypass the cave and head for the [mountain pass].")
    choice = input("> ").lower()

    if choice == 'cave':
        cave_entrance(player_name)
    elif choice == 'mountain pass':
        mountain_pass(player_name)
    else:
        print("Invalid response, respond with one of the choices in the brackets\n")
        hidden_path(player_name)

def cave_entrance(player_name):
    print("\nYou enter the cave, where you see two tunnels ahead:")
    print("1. A tunnel illuminated by glowing lights on the [left].")
    print("2. A dark tunnel with strange sounds on the [right].")
    choice = input("> ").lower()

    if choice == 'left':
        left_tunnel(player_name)
    elif choice == 'right':
        right_tunnel(player_name)
    else:
        print("Invalid response, respond with one of the choices in the brackets\n")
        cave_entrance(player_name)

def mountain_pass(player_name):
    print("\nYou bypass the cave and continue towards the mountains.")
    print("However, a sudden rockslide blocks your path.")
    print("Game Over. You didn't reach the relic.")
    game_over(player_name)

def left_tunnel(player_name):
    print("\nYou follow the glowing lights and discover the Lost Relic!")
    print(f"Congratulations, {player_name}! You've completed your adventure and found the Lost Relic.")
    print("Thanks for playing! :D\n")
    restart_game()

def right_tunnel(player_name):
    print("\nYou follow the strange sounds, only to find a dead end.")
    print("Suddenly, the cave begins to collapse!")
    game_over(player_name)

def game_over(player_name):
    print(f"\nGame Over, {player_name}. Better luck next time!\n")
    restart_game()

def restart_game():
    print("Would you like to play again? [yes] or [no]")
    choice = input("> ").lower()

    if choice == 'yes':
        start_adventure(player_name)
    elif choice == 'no':
        print("Thank you for playing! Goodbye!")
    else:
        print("Invalid response, respond with yes or no.")
        restart_game()

if __name__ == "__main__":
    # Start the adventure
    player_name, player_age = get_user_info()
    start_adventure(player_name)

