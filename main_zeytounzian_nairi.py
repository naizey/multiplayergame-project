# ITP 116, Spring 2025
# Final Project
# Name: Nairi Zeytounzian
# Email: zeytounz@usc.edu
# Filename: main_zeytounzian_nairi.py
# Description: main loop that goes through all menu options, does what user chooses

import helper
import display

def main():
    print("Welcome to our gaming hub!\n")

    data = helper.read_player_data()
    options = helper.create_options_dict()

    choice = ""
    while choice != "Q":
        display.display_user_menu(options)
        choice = helper.get_user_option(options)

        if choice == "A":
            display.display_player_by_ID(data)
        elif choice == "B":
            display.display_smallest_value(data)
        elif choice == "C":
            display.display_largest_value(data)
        elif choice == "D":
            display.display_top_scores(data)
        elif choice == "E":
            helper.find_players(data)
        elif choice == "P":
            helper.play_game(data)

    print("Goodbye!")


if __name__ == "__main__":
    main()