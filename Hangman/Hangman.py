print("Welcome to Hangman !")
wordList_def = ("Computer", "Flame", "Mathematics", "Condition", "Frigid")  # A word tuple with some default words (for default mode)
wordList_cust = [""]  # An initialized word list that will contain user input words (for custom mode)

print("Would you like to use a default set of words or run in custom mode with words of your own ?")
gameMode = input("Enter D to play in Default mode or C to play in Custom mode")
