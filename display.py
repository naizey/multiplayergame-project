# ITP 116, Spring 2025
# Final Project
# Name: Nairi Zeytounzian
# Email: zeytounz@usc.edu
# Filename: display.py
# Description: functions that display all necessary outputs (players, scores)

import pandas as pd


#display the menu to the user in a nice format
def display_user_menu(optionsDict):
    for key, value in optionsDict.items():
        print(key, "->", value)

#data param holds a single players info
def display_player(player):
    #get total score
    total = player["game1_score"] + player["game2_score"] + player["game3_score"]
    print(player["name"] + " [#" + str(player["id"]) + "]")
    print("   The game 1 score is", player['game1_score'])
    print("   The game 2 score is", player['game2_score'])
    print("   The game 3 score is", player['game3_score'])
    print("   Total score is", total, "\n")

#get the smallest value depending on score chosen
def display_smallest_value(data):
    keys = ['game1_score', 'game2_score', 'game3_score']
    print("Select from this list: ", keys)

    #ask user for input from list
    key = input("Enter a key: ").strip().lower()
    while key not in keys:
        key = input("Enter a key: ").strip().lower()

    min_val = data[key].min() #get the min value
    row = data.loc[data[key] == min_val].iloc[0] #get the row its in
    display_player(row)

#get the largest value depending on score chosen
def display_largest_value(data):
    keys = ['game1_score', 'game2_score', 'game3_score']
    print("Select from this list: ", keys)

    #ask user for input from list
    key = input("Enter a key: ").strip().lower()
    while key not in keys:
        key = input("Enter a key: ").strip().lower()

    max_val = data[key].max() #get max value
    row = data.loc[data[key] == max_val].iloc[0] #get the row
    display_player(row)

#show the player id based on the one the user chooses
def display_player_by_ID(data):
    ui = input("Enter Player ID: ").strip() #which id does user want
    if not ui.isdigit(): #if user selects a digit, not acceptable
        print("Not Accepted.")
        return
    pID = int(ui) #convert the string input to integer
    if pID < 1 or pID > 120 or pID not in data['id'].values: #must be greater than 1 below 120
        print("Not Accepted.")
        return

    row = data.loc[data['id'] == pID].iloc[0]
    display_player(row)

#show the top scores from all games
def display_top_scores(data):
    total = (data['game1_score'] + data['game2_score'] + data['game3_score']).values.tolist()
    total.sort(reverse=True) #sort list printing top scores first

    print("How many top scores (max is 100) do you want to display?")
    #get integer from user
    ui = input("Enter a number: ").strip()
    while not ui.isdigit() or not (1 <= int(ui) <= 100):
        ui = input("Enter a number: ").strip()
    top = int(ui) #get top scores

    if top > len(total): #edge case
        top = len(total)

    #loop through from i to number entered, and display the top scores
    for i in range(top):
        print(str(i + 1) + ". " + str(total[i]))
    print()

