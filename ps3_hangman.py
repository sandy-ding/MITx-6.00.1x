# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    b = False
    for c in secretWord:
        if c in lettersGuessed:
            b = True
        else:
            return False
    return b



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s = ''
    for c in secretWord:
        if c in lettersGuessed:
            s += c
        else:
            s += ' _ '
    return s



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    s = string.ascii_lowercase
    for c in lettersGuessed:
        s = s.replace(c,'')
    return s

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    mistakesMade = 0
    guessedWord = ''
    for i in range(len(secretWord)):
        guessedWord +='_ '
    r = False
    
    #print welcome
    print('Welcome to the game, Hangman!\n \
	I am thinking of a word that is ',len(secretWord),'letters long.\n \
    ------------')
    #print('------------')
    
    while mistakesMade < 8 and not r:
        
        print('You have', 8-mistakesMade, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        
        #get guess word
        guess = input('Please guess a letter:')
        guessInLowerCase = guess.lower()
        
        #check if guess is guessed before
        if not guessInLowerCase in lettersGuessed:
            lettersGuessed.append(guessInLowerCase)
        else:
            print("Oops! You've already guessed that letter: ", guessedWord)
            continue
        
        r = isWordGuessed(secretWord, lettersGuessed)
        guessedWord = getGuessedWord(secretWord, lettersGuessed)
        
        #check correctness
        #right guess
        if guessInLowerCase in secretWord:
            print('Good guess:',guessedWord)
            print('------------')
            
        #wrong guess
        else:
            mistakesMade += 1
            print('Oops! That letter is not in my word:',guessedWord)
            print('------------')
    
        
    if mistakesMade == 8:
        print('Sorry, you ran out of guesses. The word was else.')
    elif r:
        print('Congratulations, you won!')
        




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = 'bad'
hangman(secretWord)
