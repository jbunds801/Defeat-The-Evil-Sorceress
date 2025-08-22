import random


class Character:
    def __init__(
        self,
        name,
        health,
        attack_power,
        special_ability=None,
        ability_cost=None,
    ):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.special_ability = special_ability
        self.ability_cost = ability_cost

    def attack(self, opponent):
        variance = random.uniform(0.85, 1.15)
        damage = int(self.attack_power * variance)
        opponent.health -= damage
        print(f"\n{self.name} attacks {opponent.name} for {damage} damage!")

    def use_special_ability(self, opponent):
        if self.special_ability:
            ability_name, multiplier, message = self.special_ability
            variance = random.uniform(0.9, 1.1)
            damage = int(self.attack_power * multiplier * variance)
            opponent.health -= damage
            print(message.format(user=self.name, opponent=opponent.name, damage=damage))

        if self.ability_cost:
            self.health -= self.ability_cost
            print(
                f"{self.name} spent {self.ability_cost} health to use {ability_name}!"
            )


class EvilSorceress(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=200,
            attack_power=18,
            special_ability=(
                "Dark Blast",
                1.75,
                "{user} unleashes a DARK BLAST! {opponent} takes {damage} damage!",
            ),
            ability_cost=None,
        )

    def regenerate(self):
        self.health = min(self.health + 8, self.max_health)
        print(f"{self.name} regenerates 8 health!\n")


class Warrior(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=150,
            attack_power=18,
            special_ability=(
                "Critical Hit",
                1.5,
                "{user} lands a CRITICAL HIT! {opponent} takes {damage} damage!",
            ),
            ability_cost=8,
        )


class Mage(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=110,
            attack_power=26,
            special_ability=(
                "Lightning Strike",
                1.75,
                "{user} casts LIGHTNING from above! {opponent} takes {damage} damage!",
            ),
            ability_cost=6,
        )


class Rogue(Character):
    def __init__(self, name):
        super().__init__(
            name,
            health=90,
            attack_power=30,
            special_ability=(
                "Sneak Attack",
                2,
                "{user} VANISHES INTO THE SHADOWS and strikes from behind! {opponent} takes {damage} damage!",
            ),
            ability_cost=6,
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
        )
