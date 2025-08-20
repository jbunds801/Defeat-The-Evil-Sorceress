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
        #check_health(self)


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
