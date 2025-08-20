from classes import Warrior, Mage, Huntress, Rogue, Summoner

def show_instructions():
    print("Options:")
    print("1. Pick a Character")
    print("2. View Character Class Stats")
    print("3. Quit\n")


def view_stats():
    characters = [
        Warrior("Warrior"),
        Mage("Mage"),
        Huntress("Huntress"),
        Rogue("Rouge"),
        Summoner("Summoner"),
    ]
    print("\n----- Character Stats -----\n")
    for char in characters:
        special_ability_info = (
            f"{char.special_ability[0]} ({char.special_ability[1]} x damage)"
            + "\n"
            + "-" * 40
            if char.special_ability
            else "None"
        )
        print(
            f"{char.__class__.__name__}: Health = {char.health} ⁘ Attack = {char.attack_power} ⁘ Special Ability = {special_ability_info} ⁘ Special Ability Cost = {char.ability_cost}"
        )
    return create_character()


def check_health(self):
    print(f"Current Health: {self.health}/{self.max_health}")


def create_character():
    print("\nChoose your Character Class:")
    print("'W'. Warrior")
    print("'M'. Mage")
    print("'R'. Rogue")
    print("'H'. Huntress")
    print("'S'. Summoner\n")

    while True:
        class_choice = input("Enter the letter of your class choice: ").strip().lower()
        name = input("Enter your character's name: ")
        print("\n" + "-" * 40)

        if class_choice == "w":
            return Warrior(name)
        elif class_choice == "m":
            return Mage(name)
        elif class_choice == "r":
            return Rogue(name)
        elif class_choice == "h":
            return Huntress(name)
        elif class_choice == "s":
            return Summoner(name)
        else:
            print("Invalid choice, please try again.")


def battle(player, sorceress):
    print("\nYou will face off with the Evil Sorceress alone!")
    while sorceress.health > 0 and player.health > 0:
        print("\n----- Your Turn! -----")
        print("'A'. Attack")
        print("'S'. Use Special Ability")
        print("'H'. Heal")
        print("'C'. Check Health")

        choice = input("\nChoose an action: ").strip().lower()

        if choice == "a":
            player.attack(sorceress)
        elif choice == "s":
            player.use_special_ability(sorceress)
            check_health(player)
        elif choice == "h":
            pass  # Implement heal method
        elif choice == "c":
            check_health(player)
        else:
            print("Invalid choice. Try again.")

        if sorceress.health > 0:
            if choice != "c":
                sorceress.attack(player)
                sorceress.regenerate()

        if player.health <= 0:
            print(f"\n{player.name} has been defeated!")
            break

    if sorceress.health <= 0:
        print(f"\nThe Sorceress {sorceress.name} has been defeated by {player.name}!")
