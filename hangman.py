import random
# library that we use in order to choose
# on random words from a list of words

name = input("What is your name?\t\n :- ")
# Here the user is asked to enter the name first
level = int(input(f"# {name} #\tChoose difficulty:\n 1 . Easy(3 letters)"
"\n 2 . Medium(5 letters)\n 3 . Hard(7 letters)\n:-->"
))

print("Good Luck ! ", name.capitalize())

words1 = ['act','bee','cop','flu','hog','lea','pip','set','vie','cry']
words2 = ['acids','bhaji','sunday','sunny','blobs','chime','rifle','sight','wrath','zones']
words3 = ['attempt','decades','exhibit','interim','lithium','protect','quantum','several','tickets','undergo','vampire','whether']

if level == 1:
    word1 = random.choice(words1)# Function will choose one random
    


    print("Guess the characters")

    guesses = ''

    # any number of turns can be used here
    turns = 12


    while turns > 0:
        
        # counts the number of times a user fails
        failed = 0
        
        # all characters from the input
        # word taking one at a time.
        for char in word1:
            
            # comparing that character with
            # the character in guesses
            if char in guesses:
                print(char)
                
            else:
                print("_")
                
                # for every failure 1 will be
                # incremented in failure
                failed += 1
                

        if failed == 0:
            # user will win the game if failure is 0
            # and 'You Win' will be given as output
            print("You Win")
            
            # this print the correct word
            print("The word is: ", word1)
            break
        
        # if user has input the wrong alphabet then
        # it will ask user to enter another alphabet
        guess = input("guess a character:")
        
        # every input character will be stored in guesses
        guesses += guess
        
        # check input with the character in word
        if guess not in word1:
            
            turns -= 1
            
            # if the character doesn’t match the word
            # then “Wrong” will be given as output
            print("Wrong")
            
            # this will print the number of
            # turns left for the user
            print("You have", + turns, 'more guesses')
            
            
            if turns == 0:
                print("You Loose")


elif  level == 2:                
    word2 = random.choice(words2)# Function will choose one random
    print("Guess the characters")

    guesses = ''

    # any number of turns can be used here
    turns = 10


    while turns > 0:
        
        # counts the number of times a user fails
        failed = 0
        
        # all characters from the input
        # word taking one at a time.
        for char in word2:
            
            # comparing that character with
            # the character in guesses
            if char in guesses:
                print(char)
                
            else:
                print("_")
                
                # for every failure 1 will be
                # incremented in failure
                failed += 1
                

        if failed == 0:
            # user will win the game if failure is 0
            # and 'You Win' will be given as output
            print("You Win")
            
            # this print the correct word
            print("The word is: ", word2)
            break
        
        # if user has input the wrong alphabet then
        # it will ask user to enter another alphabet
        guess = input("guess a character:")
        
        # every input character will be stored in guesses
        guesses += guess
        
        # check input with the character in word
        if guess not in word2:
            
            turns -= 1
            
            # if the character doesn’t match the word
            # then “Wrong” will be given as output
            print("Wrong")
            
            # this will print the number of
            # turns left for the user
            print("You have", + turns, 'more guesses')
            
            
            if turns == 0:
                print("You Loose")
elif  level == 3:                
    word3 = random.choice(words3)# Function will choose one random
    print("Guess the characters")

    guesses = ''

    # any number of turns can be used here
    turns = 7


    while turns > 0:
        
        # counts the number of times a user fails
        failed = 0
        
        # all characters from the input
        # word taking one at a time.
        for char in word3:
            
            # comparing that character with
            # the character in guesses
            if char in guesses:
                print(char)
                
            else:
                print("_")
                
                # for every failure 1 will be
                # incremented in failure
                failed += 1
                

        if failed == 0:
            # user will win the game if failure is 0
            # and 'You Win' will be given as output
            print("You Win")
            
            # this print the correct word
            print("The word is: ", word3)
            break
        
        # if user has input the wrong alphabet then
        # it will ask user to enter another alphabet
        guess = input("guess a character:")
        
        # every input character will be stored in guesses
        guesses += guess
        
        # check input with the character in word
        if guess not in word3:
            
            turns -= 1
            
            # if the character doesn’t match the word
            # then “Wrong” will be given as output
            print("Wrong")
            
            # this will print the number of
            # turns left for the user
            print("You have", + turns, 'more guesses')
            
            
            if turns == 0:
                print("You Loose")
else:
    print("Be careful with your inputs")


print("BY SUNNY...")
