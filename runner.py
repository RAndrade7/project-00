# Condensed Adventure Game

inventory, puzzle_solved, game_over = [], False, False
current_room = "entrance"

rooms = {
    "entrance": {"desc": "You are at the entrance of a dark forest.", "exits": {"north": "cabin", "east": "cave"}, "items": ["map"], "chars": ["wolf"]},
    "cabin": {"desc": "A small cabin. Solve the puzzle to unlock the treasure.", "exits": {"south": "entrance"}, "items": ["key"], "chars": ["old_man"]},
    "cave": {"desc": "A dark cave with a chest.", "exits": {"west": "entrance"}, "items": ["sword"], "chars": []}
}

characters = {
    "wolf": {"desc": "A fierce wolf blocks your path.", "interaction": "The wolf growls threateningly."},
    "old_man": {"desc": "An old man sits by the fire.", "interaction": "Old Man: 'Solve the puzzle for the treasure.'"}
}

def show_room():
    room = rooms[current_room]
    print(f"\n{room['desc']}")
    if room["items"]: print(f"Items: {', '.join(room['items'])}")
    if room["chars"]: print(f"Characters: {', '.join(room['chars'])}")
    print(f"Exits: {', '.join(room['exits'])}")

def handle_command(command):
    global current_room, puzzle_solved, game_over
    words = command.lower().split()

    if words[0] in ["go", "move"] and words[1] in rooms[current_room]["exits"]:
        current_room = rooms[current_room]["exits"][words[1]]; show_room()

    elif words[0] == "take" and words[1] in rooms[current_room]["items"]:
        inventory.append(words[1]); rooms[current_room]["items"].remove(words[1]); print(f"You took the {words[1]}.")

    elif words[0] == "use" and words[1] in inventory:
        if words[1] == "key" and current_room == "cabin":
            rooms["cabin"]["items"].append("treasure"); print("You unlocked the treasure!")
        elif words[1] == "sword" and "wolf" in rooms[current_room]["chars"]:
            rooms[current_room]["chars"].remove("wolf"); print("You defeated the wolf!")

    elif words[0] == "talk" and words[2] in rooms[current_room]["chars"]:
        print(characters[words[2]]["interaction"])
        if words[2] == "old_man" and not puzzle_solved: solve_puzzle()

    elif words[0] == "inventory": print(f"Inventory: {', '.join(inventory) if inventory else 'nothing'}")

def solve_puzzle():
    global puzzle_solved, game_over
    if input("Riddle: 'What has keys but can't open doors?' ").lower() == "piano":
        print("Correct! You solved the puzzle."); puzzle_solved = True; game_over = True
    else: print("Wrong answer. Try again.")

def game_loop():
    show_room()
    while not game_over:
        handle_command(input("\n> "))
    print("Congratulations! You've completed the game!")

if __name__ == "__main__":
    print("Welcome to the Adventure Game!")
    game_loop()