from classes import EvilSorceress, Warrior, Mage, Huntress, Rogue, Summoner
import random


def show_instructions():
    print("\n" + "-" * 40 + "\n")
    print("\n--- Welcome to DEFEAT THE EVIL SORCORESS! ---")
    print("One brave warrior will face the Evil Sorceress in battle.")
    print("First, you must choose your character or you can view the stats of each.")
    print("At any point in the game, you can type 'quit' to exit!\n")
    print("Options:")
    print("1. Pick a Character")
    print("2. View Character Stats")
    print("3. Quit\n")


def view_stats():
    characters = [
        EvilSorceress("Evil Sorceress"),
        Warrior("Warrior"),
        Mage("Mage"),
        Huntress("Huntress"),
        Rogue("Rouge"),
        Summoner("Summoner"),
    ]
    print("\n----- Character Stats -----\n")
    for char in characters:
        special_ability_info = (
            f"{char.special_ability[0]} ( ~ {char.special_ability[1]} x attack) ⁘ Special Ability Health Cost = {char.ability_cost}"
            + "\n"
            + "-" * 120
            if char.special_ability
            else "None"
        )
        print(
            f"{char.__class__.__name__}: Health = {char.health} ⁘ Attack ~ {char.attack_power} ⁘ Special Ability = {special_ability_info}"
        )
    return create_character()


import sys


def get_input(prompt):
    user_input = input(prompt).strip().lower()
    if user_input == "quit":
        print("\nYou can run but you can't hide! See you next time!")
        sys.exit()
    return user_input


def check_health(self):
    print(f"{self.name} Health: {self.health}/{self.max_health}")

    """ # Track the number of turns since last heal
    heal_cooldown = {"turns_since_heal": 3}

    def can_heal(player):
        return player.health < player.max_health and heal_cooldown["turns_since_heal"] >= 3

    def heal(player):
        if can_heal(player):
            heal_amount = int(player.max_health * 0.40)
            player.health = min(player.health + heal_amount, player.max_health)
            print(f"\n{player.name} heals {heal_amount} points")
            heal_cooldown["turns_since_heal"] = 0
        else:
            print("\nHeal is on cooldown! You must wait before healing again.") """


def heal(player):
    heal_amount = int(player.max_health * 0.40)
    player.health = min(player.health + heal_amount, player.max_health)
    # print("\n(((o(*ﾟ▽ﾟ*)o)))\n")
    print(f"\n{player.name} heals {heal_amount} points")


def block(player, opponent):
    damage = int(opponent.attack_power * 0.15)
    player.health -= damage
    print(f"\n{player.name} blocks the attack! Damage taken: {damage}")


def create_character():
    print("\nChoose your Character Class:")
    print("'W'. Warrior")
    print("'M'. Mage")
    print("'R'. Rogue")
    print("'H'. Huntress")
    print("'S'. Summoner")

    while True:
        class_choice = (
            get_input("\nEnter the letter of your character class choice: ")
            .strip()
            .lower()
        )
        if class_choice == "w":
            char_class = Warrior
            break
        elif class_choice == "m":
            char_class = Mage
            break
        elif class_choice == "r":
            char_class = Rogue
            break
        elif class_choice == "h":
            char_class = Huntress
            break
        elif class_choice == "s":
            char_class = Summoner
            break
        else:
            print("Invalid choice, please try again.")

    while True:
        name = input("Enter your character's name: ").strip()
        if 1 <= len(name) <= 20:
            break
        print("\nName must be 1-20 characters.")

    return char_class(name)


def battle(player, sorceress):
    print("\nYou will face off with the Evil Sorceress alone!")

    turn_counter = 1
    last_heal_turn = -999  # ensures heal is available on first turn

    while sorceress.health > 0 and player.health > 0:
        print(f"\n----- Turn {turn_counter} -----")
        print("'A'. Attack")
        print("'S'. Use Special Ability")
        print("'H'. Heal")
        print("'B'. Block")

        choice = get_input("\nChoose an action: ").strip().lower()

        if choice == "a":
            player.attack(sorceress)
        elif choice == "s":
            player.use_special_ability(sorceress)
        elif choice == "h":
            # ⬇️ New cooldown check
            if turn_counter - last_heal_turn >= 3:
                heal(player)
                last_heal_turn = turn_counter
            else:
                turns_left = 3 - (turn_counter - last_heal_turn)
                print(
                    f"Heal is on cooldown! You can heal again in {turns_left} turn(s)."
                )
        elif choice == "b":
            block(player, sorceress)
        else:
            print("Invalid choice. Try again.")
            continue

        # Show health after player's turn
        if player.health > 0 and sorceress.health > 0:
            print("")
            check_health(player)
            check_health(sorceress)

        # Sorceress's turn
        if sorceress.health > 0 and player.health > 0:
            action_roll = random.random()
            if action_roll < 0.15:
                sorceress.use_special_ability(player)
            else:
                sorceress.attack(player)
            sorceress.regenerate()  # she still heals every turn, no cooldown

        # Show health after sorceress's turn
        if player.health > 0 and sorceress.health > 0:
            print("")
            check_health(player)
            check_health(sorceress)

        turn_counter += 1  # ⬅️ increment turn after both sides act

    if player.health <= 0:
        return "lose"
    if sorceress.health <= 0:
        return "win"


""" def battle(player, sorceress):
    print("\nYou will face off with the Evil Sorceress alone!")
    
    while sorceress.health > 0 and player.health > 0:
        print("\n----- Your Turn! -----")
        print("'A'. Attack")
        print("'S'. Use Special Ability")
        print("'H'. Heal")
        print("'B'. Block")

        choice = get_input("\nChoose an action: ").strip().lower()

        if choice == "a":
            player.attack(sorceress)
        elif choice == "s":
            player.use_special_ability(sorceress)
        elif choice == "h":
            heal(player)
        elif choice == "b":
            block(player, sorceress)
        else:
            print("Invalid choice. Try again.")
            continue

        if player.health > 0 and sorceress.health > 0:
            print("")
            check_health(player)
            check_health(sorceress)

        if sorceress.health > 0 and player.health > 0:
            action_roll = random.random()
            if action_roll < 0.15:
                sorceress.use_special_ability(player)
            else:
                sorceress.attack(player)
            sorceress.regenerate()

        if player.health > 0 and sorceress.health > 0:
            print("")
            check_health(player)
            check_health(sorceress)

    if player.health <= 0:
        #print(f"\n{player.name} has been defeated!")
        return "lose"
    if sorceress.health <= 0:
        #print(f"\nThe Sorceress {sorceress.name} has been defeated by {player.name}!")
        return "win"
 """
