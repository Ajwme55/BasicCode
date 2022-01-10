import Conduct_Game

print("Welcome to Hangman ! Please note that this game is case sensitive")
wordList_def = ("Computer", "Flame", "Mathematics", "Condition", "Frigid")  # A word tuple with some default words (for default mode)

print("Would you like to use a default set of words or run in custom mode with words of your own ?")
gameMode = 0
gameResult = -1  # Will state if game was won or lost

while gameMode == 0 :
    gameMode = int(input("Enter 1 to play in Default Mode or 2 to play in Custom Mode : "))  # Typecasts to int as input() gives a string

    if gameMode == 1 : 

        print("Launching game with default list of", len(wordList_def), "words")
        gameResult = Conduct_Game.Game(wordList_def)

    elif gameMode == 2 :

        latestWord = []  # THIS MAY NEED IMPROVMENT
        maxW = 10  # Editable value, the maximum number of custom words

        print("Enter upto",maxW,"words you want to use - hit enter after each word and type DONE when finished")
        newWord = input()
        if newWord == 'DONE' :
            print("Thus there are no words at all - exiting now")
            gameResult = 2  # Quit by user input
            break
        wordList_cust = [newWord]  # An initialized word list that will contain user input words (for custom mode)
        while len(wordList_cust)<maxW :
            newWord = input()
            if newWord == 'DONE' :
                break
            latestWord = [newWord]  # THIS (SEE ABOVE) MAY NEED IMPROVMENT - IS DONE TO GET THE LATEST INPUT AS A LIST INSTEAD OF A STRING
            wordList_cust = wordList_cust + latestWord
        
        print("Launching game with a custom word list of", len(wordList_cust), "words")
        gameResult = Conduct_Game.Game(wordList_cust)

    else :  # error if user puts gameMode not as 1 or 2
        print("Error,",gameMode,"is not a valid Game Mode")
        gameMode = 0

# By this point the game will be over and gameResult will be 1 if the game was won or 0 if it was lost

if gameResult == 1 : 
    print("You win !")
elif gameResult == 0 :
    print("You Lose !")
elif gameResult == 2 :
    print("You Quit !") 
else :
    print("Error detected !")  # This should not trigger
 