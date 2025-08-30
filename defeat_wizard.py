"""use kaomoji for VISUALS/styling: ╰(*°▽°*)╯  (┬┬﹏┬┬)  (((o(*ﾟ▽ﾟ*)o)))
(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧   (⓿_⓿)   {{{(>_<)}}}   (#_<-)   (►__◄)   (╯°□°）╯︵ ┻━┻
(+_+)?   are some good ones to start. have a heart <33333
that shows health, every time a player loses 20 points take away a 3"""

"""have heal amount different for each character, more heal for characters with less health?"""

"""costs 5 health to use special ability"""


import random

print("\n--- Welcome to DEFEAT THE EVIL SORCORESS! ---")
print("One brave warrior will face the Evil Sorceress in battle.")
print("First, you must choose your character class or you can view the stats of each.")
print("At any point in the game, you can type 'quit' to exit!\n")

# put a quit at anytime option


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


class Character:
    def __init__(
        self, name, health, attack_power, special_ability=None, ability_cost=None
    ):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.special_ability = special_ability
        self.ability_cost = ability_cost

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"\n{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"\n{opponent.name} has been defeated!")

    def use_special_ability(self, opponent):
        if self.special_ability:
            ability_name, multiplier, message = self.special_ability
            damage = int(self.attack_power * multiplier)
            opponent.health -= damage
            print(message.format(user=self.name, opponent=opponent.name, damage=damage))
            self.health -= self.ability_cost
            print(
                f"{self.name} spent {self.ability_cost} health to use {ability_name}!"
            )


class EvilSorceress(Character):
    def __init__(self, name):  # still need to come up with special ability
        super().__init__(
            name,
            health=160,
            attack_power=15,
            special_ability=(
                "special ability",
                2,
                "{user} insert special ability {opponent} takes {damage} damage!",
            ),
            ability_cost=None,
        )

    """make this random"""

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health!")
        check_health(self)


class Warrior(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=140,
            attack_power=25,
            special_ability=(
                "Critical Hit",
                1.5,
                "{user} lands a CRITICAL HIT! {opponent} takes {damage} damage!",
            ),
            ability_cost=7,
        )


class Mage(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=100,
            attack_power=35,
            special_ability=(
                "Lightning Strike",
                1.5,
                "{user} casts lightning from above! {opponent} takes {damage} damage!",
            ),
            ability_cost=4,
        )


class Rogue(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=80,
            attack_power=40,
            special_ability=(
                "Sneak Attack",
                1.75,
                "{user} vanishes into the shadows and strikes from behind! {opponent} takes {damage} damage!",
            ),
            ability_cost=3,
        )


class Huntress(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=120,
            attack_power=30,
            special_ability=(
                "Summon Forest Animals",
                1.5,
                "{user} calls to the forest animals to attack! {opponent} takes {damage} damage!",
            ),
            ability_cost=5,
        )


class Summoner(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=100,
            attack_power=40,
            special_ability=(
                "Summons Demons",
                1.75,
                "{user} conjures a legion of demons!",
            ),
            ability_cost=3,
        )


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
        # make this so it doesn't take damage away from the player

        else:
            print("Invalid choice. Try again.")

        if sorceress.health > 0:
            sorceress.attack(player)
            sorceress.regenerate()

        if player.health <= 0:
            print(f"\n{player.name} has been defeated!")
            break

    if sorceress.health <= 0:
        print(f"\nThe Sorceress {sorceress.name} has been defeated by {player.name}!")


def main():
    while True:
        show_instructions()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            player = create_character()
            break
        elif choice == "2":
            player = view_stats()
            break
        elif choice == "3":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice, please try again.")
    print(f"\nWelcome {player.name} the {player.__class__.__name__}!")
    sorceress = EvilSorceress("Queen Bavmorda")
    battle(player, sorceress)


if __name__ == "__main__":
    main()
