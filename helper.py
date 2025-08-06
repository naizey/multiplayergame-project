# ITP 116, Spring 2025
# Final Project
# Name: Nairi Zeytounzian
# Email: zeytounz@usc.edu
# Filename: helper.py
# Description: helper functions used to read and parse data, and select players to play the game

import pandas as pd
import display
import gameplay


#read the csv file
def read_player_data(filename = "players.csv"):
    return pd.read_csv(filename) #reads data in csv

#parse menu options in menu text file
def create_options_dict(textFileStr = "menu_options.txt"):
    menu_ops = {} #put file in dictionary var
    file = open(textFileStr, "r") #open file for read mode
    for line in file: #read file line by line
        if ":" in line:     #lines separated by a colon
            choice = line.split(":", 1)
            key = choice[0].strip().upper()
            value = choice[1].strip()
            menu_ops[key] = value #setting dictionary values
    file.close()
    return menu_ops


def get_user_option(optionsDict):
    #continuously ask user to enter a valid menu choice
    choose_from = list(optionsDict.keys())
    choice = input("Option: ").strip().upper()
    while choice not in choose_from: #if not valid keep asking
        choice = input("Option: ").strip().upper()

    #return string that is valid option entered by user
    return choice


def play_game(data):
    #get player 1 and 2 ids as input from valid ids
    ids = data["id"].values.tolist()

    #PLAYER 1 ID
    p1ID = 0
    while p1ID not in ids:
        #select player ids that are valid
        id_choice = input("Enter Player ID: ").strip()
        if id_choice.isdigit():
            num = int(id_choice)
            #must be between this range
            if 1 <= num <= 120:
                p1ID = num

    #PLAYER 2 ID
    p2ID = 0
    #while loop condition to make sure its not the same id as player 1
    while (p2ID not in ids) or (p2ID == p1ID):
        id_choice = input("Enter Player ID: ").strip()
        if id_choice.isdigit():
            num = int(id_choice)
            #id between the range
            if 1 <= num <= 120 and num != p1ID:
                p2ID = num

    #get the player names based on their ids
    p1Name = data.loc[data["id"] == p1ID, "name"].iloc[0]
    p2Name = data.loc[data["id"] == p2ID, "name"].iloc[0]

    #play the word guessing game
    print("\nPlaying Word Guessing\n")
    result = gameplay.word_guessing_game()

    #who won
    if result == "win":
        winnerID = p1ID #assign winner and loser for ids
        loserID = p2ID
        winnerName = p1Name #get their name
    else:
        winnerID = p2ID
        loserID = p1ID
        winnerName = p2Name

    #update scores + 10 for winner
    #set winners previous score to 10 since they won
    data.loc[data["id"] == winnerID, "previous score"] = 10
    #set losers previous score to 0 since they lost
    data.loc[data["id"] == loserID, "previous score"] = 0
    #increment winner game 1 score by 10
    data.loc[data["id"] == winnerID, "game1_score"] += 10

    #display who won
    print(winnerName + " wins 10 points!\n")


#find players to play the game
def find_players(data):
    category = ["name", "hobby"] #use these categories to choose player
    print("Find players based on the following attributes:", category)

    #get user input for category they want
    key = input("Enter a key: ").strip().lower()
    while key not in category: #invalid input
        key = input("Enter a key: ").strip().lower()

    #get phrase from user depending on category
    phrase = input("Enter a search phrase: ").strip().lower()

    col = data[key].astype(str).str.lower()
    contains_phrase = col.str.contains(phrase) #condition based on key selected
    filtered_data = data[contains_phrase] #store this conditioned data

    if filtered_data.empty: #make sure its not empty
        print("No player contains " + phrase + " in key " + key)
    else: #if valid, display players chosen before playing game
        count = len(filtered_data)
        print(str(count) + " player(s) contain(s) " + phrase + " in key " + key)
        for i in range(len(filtered_data)):
            row = filtered_data.iloc[i]
            display.display_player(row) #function init in display file






