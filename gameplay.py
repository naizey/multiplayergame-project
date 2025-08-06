# ITP 116, Spring 2025
# Final Project
# Name: Nairi Zeytounzian
# Email: zeytounz@usc.edu
# Filename: gameplay.py
# Description: WORD GUESSING GAME from assignment 5. Added skipping, added showing a letter as a hint, added a difficulty choice for user

import random

#function that skips the current word if they don't feel like guessing
'''
parameter is a boolean flag that tells this function that the 1 skip offered was used already
If skip was used, can't skip anymore
'''
def skip_word(skips_used):
    if skips_used: #if player already skipped
        print("A skip was already used. Can't skip again")
        return False, skips_used  #no more skipping
    else: #skip has not been used yet
        print("Skipping this word, must guess the next word.")
        return True, True  #skip this word


#function that chooses a random word using a random generator
'''
parameters are the words and hints list
'''
def random_word(words, hints):
    #index in words list. get a random word from the list of words
    random_index = random.randrange(len(words))

    #return the word at a specific index, same for hints, and the index they are located at
    return words[random_index], hints[random_index], random_index


#function that jumbles the random word that was chosen
'''
parameter is the word we want to jumble, the current word being guessed
'''
def jumble_word(word):
    word_list = list(word)
    jumbled = ""
    while word_list: #through each letter
        letter = random.choice(word_list) #get a random letter from the word
        jumbled += letter #add it to the string
        word_list.remove(letter) #remove the letter from og word to not reuse
    return jumbled #return the jumbled word

'''
jumbles the word again so its not the same jumble
'''
def rejumble(guess_word, prev_jumble):
    rejumbled = prev_jumble #set the new to the old
    if len(guess_word) > 1: #while the length of the word being guessed is greater than 1
        while rejumbled == prev_jumble: #while rejumbled is same as the old one
            rejumbled = jumble_word(guess_word) #jumble again
    return rejumbled


'''
function that is an option for a hint rather than the jumbled word
This function reveals one letter at a time of the word, like hangman
parameter is the word they are guessing, covered is the word we are returning that has the revealed letter (somewhat recursive as it is saved then another word is revealed next time the user asks)
'''
def show_a_letter(secret_word, covered):
    hidden = [] #initialize a list to hold letters that are still hidden so that it will reveal new letters each time
    for i in range(len(covered)): #go through the "letters" of covered word
        if covered[i] == "_": #if there is a blank, not shown yet
            hidden.append(i) #add it to the hidden list

    if len(hidden) > 0: #if the hidden letters list is not empty
        letter = random.choice(hidden) #select a random letter from hidden
        covered[letter] = str(secret_word[letter]) #add it to the index of the covered word

    return covered #return the newly revealed letter with the word


#a function that adds the feature of choosing a difficulty level for the guessing game
def select_difficulty(word_count):
    #ask the user for the difficulty level of the word they want to guess based on how many guesses you can have
    print("Choose a difficulty level: easy, medium, or HARD")
    level = input("Difficulty: ").strip().lower()
    while level not in ("easy", "medium", "hard"):
        level = input("Difficulty: ").strip().lower()

    if level == "easy":
        return word_count * 10 #this is so that the number of guesses is a lot
    elif level == "medium":
        return word_count * 2 #a lot less
    else:  #hard level
        return word_count #very little since the level is hard

#main gameplay function/logic
def word_guessing_game():
    words = ["traveler", "matcha", "candy", "python", "beach", "printer", "tangerine"] #words list
    hints = ["horse", "drink", "snickers", "coding", "sandy", "3D", "orange"] #hints list

    print(len(words), "word(s) to guess in the guessing game.\n")

    #the guess limit is determined by the difficulty the user selected
    guess_limit = select_difficulty(len(words))
    #guess count counter
    total_guesses = 0
    #this is the skip flag used in the skip function that can only be used once
    skip_used = False
    #counts how many hints were used and reveals at the end
    hints_used = 0
    #what this function returns
    result = "win"

    #while there are words left in the list and player hasn't lost yet
    while len(words) > 0 and result == "win":
        #get random word from function
        guess_word, hint, random_index = random_word(words, hints)
        #sets covered to all underscores the size of the word they are guessing
        covered = ["_"] * len(guess_word)

        print("A random word has been picked for you, and it has", len(guess_word), "letters.")

        #jumble the word
        jumbled = jumble_word(guess_word)
        print("The jumbled version of the word is \'" + jumbled + "\'\n")

        #how many guesses has the user used, depends for if thy win or los
        guess_count = 0
        #have they guessed the word yet
        word_found = False
        #only allowed one skip (flag)
        word_skipped = False

        guess = input("Enter your guess or select 'skip': ").strip().lower()
        if guess != "skip": #if they didn't use the skip then incremenet guess counters
            guess_count += 1
            total_guesses += 1


        #while the word isn't found, they haven't skipped and the guess limit for the difficulty chosen isn't exceeded
        while (not word_found) and (not word_skipped) and (total_guesses < guess_limit):
            if guess == "skip": #if they skip, then go skip
                skip_now, skip_used = skip_word(skip_used)
                if skip_now:
                    word_skipped = True
                else:
                    guess = input("Enter your guess or select 'skip': ").strip().lower()
            else: #if not skip
                if guess == guess_word: #if they guess the word, then its correct
                    word_found = True
                    print("Correct, the number of guesses was", guess_count, "\n")
                else:
                    print("Your guess is incorrect")

                    #if they don't guess right, ask for a hint, there are two types of hints you can have
                    want_hint = input("Do you want a hint (y or n)? ").strip().lower()
                    while want_hint not in ("y", "n"):
                        want_hint = input("Do you want a hint (y or n)? ").strip().lower()

                    if want_hint == "y":
                        #aif they want a hint, show a letter? get user input
                        hint_choice = input("Hint options: j: jumble word, s: show one letter, h: hint word - ").strip().lower()
                        while hint_choice not in ("j", "s", "h"):
                            hint_choice = input("Enter j, s, or h").strip().lower()

                        if hint_choice == "j": #if they choose j
                            #jumble the word and increment hints used
                            jumbled = rejumble(guess_word, jumbled)
                            print("The jumbled word is \'" + jumbled + "\'\n")
                            hints_used += 1

                        elif hint_choice == "s": #if they choose s
                            #show the letter and increment hints used
                            covered = show_a_letter(guess_word, covered)
                            print("Revealed letters: " + " ".join(covered))
                            hints_used += 1

                        elif hint_choice == "h":
                            print("The hint is '" + hint + "'")
                            hints_used += 1

                        print() #no hint

                    #if guesses used is less than the limit
                    if total_guesses < guess_limit - 1:
                        #can guess more
                        guess = input("Enter your guess: or select 'skip': ").strip().lower()
                        if guess != "skip":
                            guess_count += 1
                            total_guesses += 1
                    else:
                        total_guesses = guess_limit

        #lose case, word isn't found, not skipped, and guesses exceed limit
        if (not word_found) and (not word_skipped) and (total_guesses >= guess_limit):
            result = "lose"
        else:
            #if they won, then remove that word and its hint
            words.pop(random_index)
            hints.pop(random_index)

            #display words left to guess
            if len(words) > 0:
                print(len(words), "word(s) to guess in the guessing game.\n")

    #win case
    if result == "win":
        print("You guessed all the words! ")
    #lose case
    else:
        print("Game over - didn't guess all words")
    #show hints used
    print("You used", hints_used, "hints in total.")
    return result





