def Game(wordList):
    import random
    gameWord = wordList[random.randrange(0,len(wordList))]  # Gives the gameword, chosen randomly from list given

    lenWord = len(gameWord)  # An often used quantity saved as a variable for readability 
    gameWord_letterStatus = [0] * lenWord  # A list that holds if each letter of the word has been discovered (by default nothing is discovered and is all 0s)
    runStatus = 1  # 1 if the game is the game running, 0 if it over
    lives = 10  # Editable value, number of lives given to player before "hanging"

    while runStatus == 1 :
        print("")  # Some spacing

        print("Try to guess the word :",end =' ')  # End set to blank so as to not go to a new line
        for x in range(0,lenWord) :  # Loop to display whole word
            if gameWord_letterStatus[x] == 0 :
                print("_",end =' ')
            elif gameWord_letterStatus[x] == 1 :
                print(gameWord[x],end =' ')
            else :
                print("Error detected (CODE 3)")  # This should not happen
                Result = 3
                break

        print(".Now guess a letter that belongs :",end =' ')  # NEED TO ADD CHECK TO MAKE SURE INPUT IS ONE LETTER + CHECK TO AVOID DUPLICATE INPUTS
        guess = input()
        badguess = 1  # If a match is found anywhere in the word the guess will no longer be bad
        for x in range(0,lenWord) :  # Loop to check through whole word if guess letter is found
            #print(gameWord[x],end =' ')  # THIS IS A DEBUGGING TOOL, KEEP IT COMMENTED OUT - displays the gameWord letter by letter
            if gameWord[x] == guess :  # match found, guess is good
                gameWord_letterStatus[x] = 1
                badguess = 0  
        if badguess == 0 :
            print("Good job, this letter was found")
        else : # badguess has to be 1 here
            lives = lives-1  # Player loses 1 life due to wrong guess
            print("Sorry, that letter was not found, you have",lives,"lives remaining")

        if lives == 0 :
            print("Out of lives ! The man is hanged !")
            Result = 0
            runStatus = 0  # Not actually needed due to break
            break

        if 0 in gameWord_letterStatus :  # Any letters still not discovered
            print("There are more letters to find !") 
        else :  # All values in gameWord_letterStatus have been set to 1 (cannot be anything else) and thus word is found
            print("Wow you found all the letters for the word",gameWord,"- the man is saved !")
            Result = 1
            runStatus = 0
    

    return Result
