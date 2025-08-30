import random
import sys

# outside of classes so it can be changed at anytime to update dynamically
heal_percent = 0.50


class Character:
    def __init__(
        self,
        name,
        health,
        attack_power,
        special_ability=None,
        ability_cost=None,
        block_ability=None,
        block_strength=None,
    ):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.special_ability = special_ability
        self.ability_cost = ability_cost
        self.block_ability = block_ability
        self.block_strength = block_strength
        self.is_blocking = False  # ensures block happens after opponent attacks
        self.next_heal_turn = 1  # implements turn counter for heal

    def attack(self, opponent):
        damage = int(self.attack_power * random.uniform(0.85, 1.15))
        print(f"\n{self.name} attacks {opponent.name} for {damage} damage!")
        opponent.take_damage(damage)

    def use_special_ability(self, opponent):
        ability_name, multiplier, message = self.special_ability

        # prevent special ability use if health is too low
        if self.ability_cost and self.health <= self.ability_cost:
            print(
                f"\n{self.name} is too weak to use {ability_name}! (Needs more health) Choose again"
            )
            return False

        damage = int(self.attack_power * multiplier * random.uniform(0.9, 1.1))
        print(
            "\n" + message.format(user=self.name, opponent=opponent.name, damage=damage)
        )
        opponent.take_damage(damage)

        if self.ability_cost:
            self.health -= self.ability_cost
            print(f"{self.name} spent {self.ability_cost} health to use {ability_name}")

        return True

    # methods to implement turn counting for heal cooldown
    def heal(self, current_turn, cooldown=5):
        if current_turn >= self.next_heal_turn:
            amount = int(self.max_health * heal_percent)
            self.health = min(self.health + amount, self.max_health)
            print(f"\n{self.name} heals {amount} points!")
            self.next_heal_turn = current_turn + cooldown
        else:
            print(
                f"Heal is on cooldown! Available in {self.next_heal_turn - current_turn} turn(s). Choose another action."
            )
            return False
        return True

    def use_block(self):
        self.is_blocking = True
        print(
            f"\n{self.name} prepares to block the next attack with their {self.block_ability}!"
        )

    def take_damage(self, amount):
        if self.is_blocking:
            reduced = int(amount * (1 - self.block_strength))
            print(
                f"{self.name} blocks with {self.block_ability}! Damage taken: {reduced}"
            )
            self.health -= reduced
            self.is_blocking = False
        else:
            self.health -= amount

        if self.health < 0:
            self.health = 0

    # statement used to see stats after each turn
    def check_health(self):
        print(f"{self.name} Health: {self.health}/{self.max_health}")


class EvilSorceress(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=200,
            attack_power=20,
            special_ability=(
                "Dark Blast",
                1.75,
                "{user} unleashes a DARK BLAST! for {damage} damage!",
            ),
        )

    def regenerate(self):
        self.health = min(self.health + 8, self.max_health)
        print(f"{self.name} regenerates 8 health!")


class Warrior(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=150,
            attack_power=25,
            special_ability=(
                "Critical Hit",
                1.65,
                "{user} lands a CRITICAL HIT! {opponent} takes {damage} damage!",
            ),
            ability_cost=7,
            block_ability="SHIELD OF DESTINY",
            block_strength=0.70,
        )


class Mage(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=110,
            attack_power=27,
            special_ability=(
                "Lightning Strike",
                1.75,
                "{user} casts LIGHTNING from above! {opponent} takes {damage} damage!",
            ),
            ability_cost=6,
            block_ability="MAGIC FORCEFIELD",
            block_strength=0.80,
        )


class Rogue(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=100,
            attack_power=35,
            special_ability=(
                "Sneak Attack",
                2,
                "{user} VANISHES INTO THE SHADOWS and strikes from behind! {opponent} takes {damage} damage!",
            ),
            ability_cost=6,
            block_ability="PHANTOM DODGE",
            block_strength=0.90,
        )


class Huntress(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=125,
            attack_power=24,
            special_ability=(
                "Summon Forest Animals",
                1.5,
                "{user} calls to the FOREST ANIMALS to attack! {opponent} takes {damage} damage!",
            ),
            ability_cost=7,
            block_ability="FLASH MOVE",
            block_strength=0.85,
        )


class Summoner(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=110,
            attack_power=25,
            special_ability=(
                "Summons Demons",
                1.75,
                "{user} conjures a LEGION OF DEMONS! {opponent} takes {damage} damage!",
            ),
            ability_cost=6,
            block_ability="GUARDIAN WRAITH",
            block_strength=0.85,
        )


def show_instructions():
    print("\n" + "-" * 40 + "\n")
    print("\n--- Welcome to DEFEAT THE EVIL SORCERESS! ---")
    print("One brave warrior will face the Evil Sorceress in battle.")
    print("First, you must choose your character or you can view the stats of each.")
    print("At any point in the game, you can type ' QUIT' to exit!\n")
    print("Options:")
    print("1. Pick a Character")
    print("2. View Character Stats\n")


# implemented so player can quit game at any time
def get_input(prompt):
    user_input = input(prompt).strip().lower()
    if user_input == "quit":
        print("\nYou can run but you can't hide! See you next time!")
        sys.exit()
    return user_input


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

        classes = {"w": Warrior, "m": Mage, "r": Rogue, "h": Huntress, "s": Summoner}
        if class_choice in classes:
            char_class = classes[class_choice]
            break
        print("Invalid choice, try again.")

    while True:
        name = input("Enter your character's name: ").strip()
        if 1 <= len(name) <= 20:
            break
        print("\nName must be 1-20 characters.")

    return char_class(name)


def view_stats():
    characters = [
        EvilSorceress("Evil Sorceress"),
        Warrior("Warrior"),
        Mage("Mage"),
        Huntress("Huntress"),
        Rogue("Rogue"),
        Summoner("Summoner"),
    ]

    # prints out each character classes stats. uses template literals for future class additions
    print("\n----- Character Stats -----\n")
    for char in characters:
        if char.special_ability:
            if char.ability_cost is None:
                cost = 0
            else:
                cost = char.ability_cost
            special_ability_info = f"{char.special_ability[0]} ( ~ {char.special_ability[1]} x attack), Cost = {cost} Health)"
        else:
            special_ability_info = "None"

        if char.block_strength:
            block_info = f"{char.block_ability} ({int(char.block_strength * 100)}%)"
        else:
            block_info = "None"
        print(
            f"{char.__class__.__name__}:  ⁘ Health = {char.health} ⁘ Attack ~ {char.attack_power}\n⁘ Special Ability = {special_ability_info} ⁘ Block = {block_info}"
            + ("\n" + "-" * 120)
        )
    print(f"*** Each player can heal {int(heal_percent * 100)}% every 5th turn! ***")
    print("-" * 120)
    return create_character()


# wrapper for check_health
def show_health_stats(*characters):
    for char in characters:
        char.check_health()


def battle(player, sorceress):
    print("\nYou will face off with the Evil Sorceress alone!")

    # sets turn counter for heal cooldown
    turn_counter = 1

    while sorceress.health > 0 and player.health > 0:

        # shows if player can heal or not in line 307
        heal_text = (
            "(available)"
            if player.next_heal_turn <= turn_counter
            else f"(in {player.next_heal_turn - turn_counter} turns)"
        )
        print(f"\n----- Your Turn! -----")
        print("'A'. Attack")
        print("'S'. Use Special Ability")
        print(f"'H'. Heal {heal_text}")
        print("'B'. Block")

        choice = get_input("\nChoose an action: ").strip().lower()

        if choice == "a":
            player.attack(sorceress)
        elif choice == "s":
            if not player.use_special_ability(sorceress):
                continue
        elif choice == "h":
            if not player.heal(turn_counter):
                continue
        elif choice == "b":
            player.use_block()
        else:
            print("Invalid choice. Try again.")
            continue
        print("")
        show_health_stats(player, sorceress)

        # Sorceress's turn
        if sorceress.health > 0:
            if random.random() < 0.15:
                sorceress.use_special_ability(player)
            else:
                sorceress.attack(player)
            sorceress.regenerate()

        print("")
        show_health_stats(player, sorceress)

        turn_counter += 1

    if player.health == 0:
        print(
            f"\n{player.name} was defeated by {sorceress.name}... Darkness spreads across the land."
        )
    if sorceress.health == 0:
        print(
            f"\nVictory! {player.name} has defeated {sorceress.name} and saves the realm!"
        )


def main():
    while True:
        while True:
            show_instructions()
            choice = get_input("Enter your choice: ")
            if choice == "1":
                player = create_character()
                break
            elif choice == "2":
                player = view_stats()
                break
            else:
                print("Invalid choice, please try again.")

        print("\n" + "-" * 40)
        print(f"\nWelcome {player.name} the {player.__class__.__name__}!")
        sorceress = EvilSorceress("Queen Bavmorda")
        battle(player, sorceress)

        choice = get_input("\nWould you like to play again? (y/n): ").strip().lower()

        while True:
            if choice == "n":
                print("Thanks for playing! Goodbye!")
                sys.exit()
            elif choice == "y":
                break
            else:
                print("Invalid choice, try again")


if __name__ == "__main__":
    main()
