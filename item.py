def start_game():
    print("Welcome to the Enchanted Village!")
    print("You find yourself at a crossroads in the village.")
    print("To your left is a cozy cottage, and to your right is a bustling market.")
    
    choice = input("Do you want to go left to the cottage or right to the market? (left/right) ").strip().lower()
    
    if choice == "left":
        cottage()
    elif choice == "right":
        market()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def cottage():
    print("\nYou approach the cozy cottage. The smell of fresh bread fills the air.")
    print("An old woman is sitting on the porch, knitting.")
    
    choice = input("Do you want to talk to her? (yes/no) ").strip().lower()
    
    if choice == "yes":
        talk_to_npc()
    elif choice == "no":
        print("You decide to leave the cottage.")
        start_game()
    else:
        print("Invalid choice. Please try again.")
        cottage()

def market():
    print("\nYou walk into the bustling market filled with vibrant colors and lively chatter.")
    print("You see a merchant selling exotic fruits.")
    
    choice = input("Do you want to talk to the merchant? (yes/no) ").strip().lower()
    
    if choice == "yes":
        talk_to_npc()
    elif choice == "no":
        print("You decide to leave the market.")
        start_game()
    else:
        print("Invalid choice. Please try again.")
        market()

def talk_to_npc():
    print("\nThe NPC smiles warmly at you.")
    print("She says, 'Hello traveler! Welcome to our village. What brings you here?'")
    
    response = input("You can say: 'I'm looking for adventure!' or 'Just passing by.' ").strip().lower()
    
    if response == "i'm looking for adventure!":
        print("The NPC replies, 'Ah, a brave soul! There's a legend of treasure hidden in the forest. Be careful on your journey!'")
    elif response == "just passing by.":
        print("The NPC nods and says, 'Well, safe travels! There's always something to see in our village.'")
    else:
        print("The NPC looks confused. 'I don't understand what you mean.'")
    
    print("\nWhat would you like to do now?")
    next_action = input("You can 'explore' the village more or 'leave' the village. ").strip().lower()
    
    if next_action == "explore":
        start_game()
    elif next_action == "leave":
        print("You wave goodbye and leave the village.")
    else:
        print("Invalid choice. Please try again.")
        talk_to_npc()

# Start the game
start_game()
