import Conduct_Game

print("Welcome to Hangman !")
wordList_def = ("Computer", "Flame", "Mathematics", "Condition", "Frigid")  # A word tuple with some default words (for default mode)

print("Would you like to use a default set of words or run in custom mode with words of your own ?")
gameMode = 0
gameResult = -1  # Will state if game was won or lost

while gameMode == 0 :
    gameMode = input("Enter 1 to play in Default Mode or 2 to play in Custom Mode : ")  # APPEARS TO NOT UPDATE gameMode ????

    if gameMode == 1 : 
        print("Launching game with default list of", len(wordList_def), "words")
        gameResult = Conduct_Game.Game(wordList_def)
    elif gameMode == 2 :
        print("Enter upto 10 words you want to use - hit enter after each word ! ")
        newWord = input()
        wordList_cust = [newWord]  # An initialized word list that will contain user input words (for custom mode)
        while len(wordList_cust<10) :
            newWord = input()
            wordList_cust = wordList_cust + newWord
        print("Launching game with a custom word list of ", len(wordList_cust), "words")
        gameResult = Conduct_Game.Game(wordList_cust)
    else :  # error if user puts gameMode not as 1 or 2
        print("Error,",gameMode,"is not a valid Game Mode")
        gameMode = 0

# By this point the game will be over and gameResult will be 1 if the game was won or 0 if it was lost

if gameResult == 1 : 
    print("You win !")
elif gameResult == 0 :
    print("You Lose !")
else :
    print("Error detected in game result")  # This should not trigger
 