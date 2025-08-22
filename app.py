from classes import EvilSorceress
from actions import show_instructions, get_input, create_character, view_stats, battle


def main():
    while True:
        while True:
            show_instructions()
            choice = get_input("Enter your choice: ").strip().lower()
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
        print("\n" + "-" * 40)
        print(f"\nWelcome {player.name} the {player.__class__.__name__}!")
        sorceress = EvilSorceress("Queen Bavmorda")

        result = battle(player, sorceress)

        if result == "win":
            print(
                f"\nVictory! {player.name} has defeated {sorceress.name} and saved the realm!"
            )
        else:
            print(
                f"\n{player.name} was defeated by {sorceress.name}... Darkness spreads across the land."
            )

        choice = input("\nWould you like to play again? (y/n): ").strip().lower()
        if choice != "y":
            print("Thanks for playing! Goodbye!")
            return


if __name__ == "__main__":
    main()
