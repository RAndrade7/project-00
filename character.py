class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = False
        
    def recive_item(self, item):
        self.recived = True
        self.append(item)
        print(f"{self.name} says: {Thank you for the {item.name} I will treasure it forever}")