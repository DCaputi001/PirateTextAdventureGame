rooms = {
    'Buccanner Bay': {'South': 'Treasure Cove', 'Item': 'Grenado'},
    'Treasure Cove': {'North': 'Buccanner Bay', 'South': 'Jolly Roger Isle', 'East': 'Skull Island'},
    'Jolly Roger Isle': {'North': 'Treasure Cove', 'East': "Kraken's Lair", 'Item': 'Eyepatch'},
    "Kraken's Lair": {'West': 'Jolly Roger Isle', 'Boss': 'Kraken'},
    'Skull Island': {'North': 'Cutlass Cay', 'East': "Blackbeards Cove", 'West': 'Treasure Cove', 'Item': 'Pirate Hat'},
    "Blackbeards Cove": {'West': 'Skull Island', 'Item': 'Pistol'},
    'Cutlass Cay': {'East': 'Mermaid Lagoon', 'South': 'Skull Island', 'Item': 'Cutlass'},
    'Mermaid Lagoon': {'West': 'Cutlass Cay', 'Item': 'Axe'}
}

DIRECTIONS = ['North', 'South', 'East', 'West']
EXIT_COMMAND = "Exit"
VALID_INPUTS = DIRECTIONS + [EXIT_COMMAND]
INVALID_DIRECTION = "That is not a valid direction. You need to enter one of: " + str(VALID_INPUTS) + "."
CANNOT_GO_THAT_WAY = "You cannot venture that way!"
GAME_OVER = "Thanks for playing."
EXIT_ROOM_SENTINEL = "exit"

# Additional global variables
inventory = []  # List to track inventory
current_room = "Treasure Cove"  # Tracks current room


# Function to display item descriptions when near an item
def display_item_description():
    nearby_item = rooms[current_room].get("Item")
    if nearby_item and nearby_item not in inventory:
        article = "an" if nearby_item[0].lower() in 'aeiou' else "a"
        print(f"You see {article} {nearby_item} nearby.")


# Function to display player's status
def display_status():
    print(f"You are in {current_room}")
    print(f"Inventory: {inventory}")
    print('-' * 27)


# Function to handle movement between rooms
def move(direction):
    global current_room
    if direction in rooms[current_room]:
        current_room = rooms[current_room][direction]
        print(f"You travel {direction}")
    else:
        print("You can't go that way.")


# Function to handle player's movement and actions
def navigate(current_room: str, user_input: str):
    next_room = current_room
    err_msg = ''

    # Check if the user wants to exit the game
    if user_input.lower() == EXIT_COMMAND.lower():
        err_msg = GAME_OVER
        next_room = EXIT_ROOM_SENTINEL
    else:
        # Check if the user's input is a valid direction
        if user_input not in VALID_INPUTS:
            err_msg = INVALID_DIRECTION
        else:
            # Check if there is a room in the given direction
            if user_input in rooms[current_room]:
                next_room = rooms[current_room][user_input]
            else:
                err_msg = CANNOT_GO_THAT_WAY
    return next_room, err_msg


# Function to show game instructions
def prompt():
    print('\t\tWelcome to the Pirate Text Adventure Game\n\n\
You are a Pirate seeking revenge for your crew that was devoured by the KRAKEN!!!\n\
To be successful you must search nearby islands and collect all six items.\n\
But be careful, the fierce Kraken is never far.\n\n\
Moves:\t\'In order to move type: (go south, go north, go east, go west).\n\
\t\'To pick up an item you see type: get (item name). \n\
\t\'exit\' (quit the game)\n')


# Game loop
def main():
    global current_room  # Add this line to indicate that 'current_room' is a global variable

    def game_loop():
        global current_room  # Use global variable to track the current room
        current_room = "Treasure Cove"
        inventory.clear()
        # Show game instructions at the beginning
        prompt()

        while True:
            display_status()

            # Check for boss encounter in "Kraken's Lair"
            if current_room == "Kraken's Lair" and "Boss" in rooms[current_room]:
                if len(inventory) < 6:
                    print(f"GAME OVER!!! You lost a fight with {rooms[current_room]['Boss']}.")
                    break
                else:
                    print(f"CONGRATULATIONS!!! You have slain the {rooms[current_room]['Boss']}!")
                    break

            display_item_description()
            # Prompt the user to input a direction and convert it to lowercase for functionality.
            user_input = input("Enter your move (e.g., 'go north', 'get item', 'exit'):\n").lower()
            # Split the input into a list of words.
            user_input = user_input.split()
            # Extract the first word from the list.
            action = user_input[0]
            # Check for appropriate action
            if action == "go":
                # Check if the user specified a direction.
                if len(user_input) < 2:
                    # If a direction is missing ask the user to specify a direction.
                    print("Please specify a direction (e.g., 'go north', 'go south', 'go east', 'go west').")
                    continue
                # Extract the direction from the user input.
                direction = user_input[1].title()
                # Call the navigate function to move to the next room.
                next_room, err_msg = navigate(current_room, direction)
                # Check if there is an error moving in specified direction.
                if err_msg == CANNOT_GO_THAT_WAY:
                    print(err_msg)
                else:
                    # If move was successful, update the current_room to the next room.
                    current_room = next_room
            elif action == "get":
                # If the action is "get", check if the user specified an item.
                if len(user_input) < 2:
                    # If the item is missing, prompt the user to specify an item and continue the loop.
                    print("Please specify an item (e.g., 'get itemname').")
                    continue
                # Extract the item name from the user input and convert it to title case.
                item = " ".join(user_input[1:]).title()
                # Check if the item is available in the current room.
                if "Item" in rooms[current_room] and rooms[current_room]["Item"] == item:
                    # If the item is available, check if the player already has the item in the inventory.
                    if item not in inventory:
                        # If the player doesn't have the item, add it to the inventory and print a success message.
                        inventory.append(item)
                        print(f"{item} retrieved!")
                    else:
                        # Print a message if the player already has the item.
                        print(f"You already have the {item}.")
                else:
                    # Print message if the item is not in current room.
                    print(f"Can't find {item}.")
            # Print message if user decides to exit the game.
            elif action == "exit":
                print("You exited the game. Come back soon!!!")
                break
            else:
                # If the action is not recognized, print a message indicating an invalid command.
                print("Invalid command.")

    while True:
        game_loop()
        replay = input("Do you want to play again? (yes/no): ").lower()
        if replay != 'yes':
            print(GAME_OVER)
            break

main()
