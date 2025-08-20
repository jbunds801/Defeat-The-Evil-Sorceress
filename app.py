"""use kaomoji for VISUALS/styling: ╰(*°▽°*)╯  (┬┬﹏┬┬)  (((o(*ﾟ▽ﾟ*)o)))
(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧   (⓿_⓿)   {{{(>_<)}}}   (#_<-)   (►__◄)   (╯°□°）╯︵ ┻━┻
(+_+)?   are some good ones to start. have a heart <33333
that shows health, every time a player loses 20 points take away a 3"""

"""have heal amount different for each character, more heal for characters 
with less health? gets more health if they're health is already up, less health if it already low"""

"""show sorceress health after each turn, which I thought it was but now it isn't. fix this.
or, make it show it shows both sides health """

"""make the sorceress harder to defeat"""


from classes import EvilSorceress
from actions import show_instructions, create_character, view_stats, battle
import random

print("\n--- Welcome to DEFEAT THE EVIL SORCORESS! ---")
print("One brave warrior will face the Evil Sorceress in battle.")
print("First, you must choose your character class or you can view the stats of each.")
print("At any point in the game, you can type 'quit' to exit!\n")

# put a quit at anytime option


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
