# CSIT 104: Python Programming I - Midterm Project
# Name: Jannathy 
# Project Title: Choose Your Own Adventure - Covert Ops: Special Forces Mission
# Summary: Theme is similar to Black Ops 
# makes decisions to complete a mission with 8 possible endings based on different choices.

def start_mission():
    """Initial scenario: starting point of the military mission."""
    print("\nYou are a special forces soldier, deep behind enemy lines.")
    print("Your mission is to infiltrate the enemy base, retrieve critical intel, and make it out alive.")
    print("Ahead of you, two paths present themselves.")
    print("To your left, a narrow alley leads toward a heavily fortified bunker.")
    print("To your right, an open field lies ahead, with snipers lurking in the distance.\n")
    
    # First decision point
    choice = input("Do you go left toward the bunker or right across the field? (left/right): ").lower()
    
    if choice == "left":
        go_left()
    elif choice == "right":
        go_right()
    else:
        print("Invalid input! Please type 'left' or 'right'.")
        start_mission()  # Loop back to initial scenario for invalid input


def go_left():
    """Path leads to the fortified bunker."""
    print("\nYou choose to move toward the bunker. As you approach, you notice armed guards patrolling.")
    choice = input("Do you take out the guards silently or plant a bomb to cause a distraction? (silent/bomb): ").lower()

    if choice == "silent":
        take_out_guards_silently()
    elif choice == "bomb":
        plant_bomb()
    else:
        print("Invalid input! Please type 'silent' or 'bomb'.")
        go_left()  # Repeat choice if input is invalid


def take_out_guards_silently():
    """Player attempts to silently take out enemy guards."""
    print("\nYou move swiftly and silently, taking out the guards one by one.")
    print("You make your way into the bunker undetected.\n")
    choice = input("Do you hack the security system or search for intel manually? (hack/search): ").lower()

    if choice == "hack":
        ending_hack_successful()
    elif choice == "search":
        ending_found_intel()
    else:
        print("Invalid input! Please type 'hack' or 'search'.")
        take_out_guards_silently()  # Loop back for invalid input


def plant_bomb():
    """Player plants a bomb to cause a distraction."""
    print("\nYou plant a bomb and cause an explosion. The guards scramble in confusion.")
    print("But the explosion has drawn too much attention, and reinforcements arrive!\n")
    choice = input("Do you escape through the back or fight off the reinforcements? (escape/fight): ").lower()

    if choice == "escape":
        ending_escape()
    elif choice == "fight":
        ending_captured()
    else:
        print("Invalid input! Please type 'escape' or 'fight'.")
        plant_bomb()  # Loop back for invalid input


def go_right():
    """Path leads across the open field with snipers."""
    print("\nYou choose to cross the open field, dodging sniper fire along the way.")
    print("You see an enemy sniper in the distance, locking on to you.\n")
    choice = input("Do you engage the sniper or call for air support? (engage/support): ").lower()

    if choice == "engage":
        engage_sniper()
    elif choice == "support":
        call_air_support()
    else:
        print("Invalid input! Please type 'engage' or 'support'.")
        go_right()  # Loop back for invalid input


def engage_sniper():
    """Player engages the sniper directly."""
    print("\nYou take a deep breath and engage the sniper.")
    print("Your shot hits its mark, and you proceed toward the enemy base unharmed.\n")
    choice = input("Do you proceed stealthily or storm the base? (stealth/storm): ").lower()

    if choice == "stealth":
        ending_stealth_success()
    elif choice == "storm":
        ending_heavy_resistance()
    else:
        print("Invalid input! Please type 'stealth' or 'storm'.")
        engage_sniper()  # Loop back for invalid input


def call_air_support():
    """Player calls for air support."""
    print("\nYou call for air support, and moments later, jets fly overhead, taking out the sniper.")
    print("With the path clear, you proceed to your objective.\n")
    choice = input("Do you retrieve the intel or destroy the base? (retrieve/destroy): ").lower()

    if choice == "retrieve":
        ending_retrieve_intel()
    elif choice == "destroy":
        ending_destroy_base()
    else:
        print("Invalid input! Please type 'retrieve' or 'destroy'.")
        call_air_support()  # Loop back for invalid input


# Ending scenarios
def ending_hack_successful():
    """Player successfully hacks the enemy system."""
    print("\nEnding 1: You hack the security system, retrieve the critical intel, and escape undetected. Mission successful!")
    end_game()


def ending_found_intel():
    """Player finds the intel manually."""
    print("\nEnding 2: You search the bunker and find the intel. With the mission complete, you make your escape!")
    end_game()


def ending_escape():
    """Player escapes after causing a distraction."""
    print("\nEnding 3: You escape through the back, but the mission is incomplete. You failed to retrieve the intel.")
    end_game()


def ending_captured():
    """Player is captured by enemy reinforcements."""
    print("\nEnding 4: You try to fight the reinforcements, but you're outnumbered and captured. Mission failed.")
    end_game()


def ending_stealth_success():
    """Player succeeds with stealth approach."""
    print("\nEnding 5: You successfully infiltrate the base using stealth and retrieve the intel without being detected.")
    end_game()


def ending_heavy_resistance():
    """Player faces heavy resistance after storming the base."""
    print("\nEnding 6: You storm the base but face heavy resistance. After a fierce battle, you're forced to retreat.")
    end_game()


def ending_retrieve_intel():
    """Player retrieves the intel after calling air support."""
    print("\nEnding 7: With air support clearing the way, you retrieve the intel and make your escape.")
    end_game()


def ending_destroy_base():
    """Player destroys the enemy base."""
    print("\nEnding 8: You plant explosives and destroy the enemy base, taking out their operations completely. Mission accomplished!")
    end_game()


def end_game():
    """End the game."""
    print("\nThe mission ends here. Thank you for playing!")
    exit()


# Start the mission
start_mission()
