import random
words = {
    'fiveLetterWords': ['chair', 'table', 'watch', 'skate', 'blend'],
    'sixLetterWords': ['banana', 'bright', 'frozen', 'bucket', 'muffin'],
    'sevenLetterWords': ['amazing', 'journey', 'whistle', 'fantasy', 'rainbow'] 
}

guessedLetters = []
displayWord= ''

def pickWord():
 x = random.choice(list(words.keys()))
 word_list = words[x]
 hangmanWord = random.choice(word_list)
 print ("\n"+ "This a " + str(len(hangmanWord)) + " letter word.")
 return hangmanWord

def loseLife(answer, life):
    if answer is True:
        return life
    else:
        life -= 1
        print("You now have " + str(life) + " lives.")
        return life

def askLetter():
    while True:
        letter = input('\n'+"Enter a letter of the alphabet as a guess: " + '\n')
        if len(letter) == 1 and letter.isalpha():
            if letter in guessedLetters:
                print("You've already guessed that letter! ")
            else:
                guessedLetters.append(letter) 
                return letter
        else:
            print("Please enter a single letter of the alphabet!" + '\n')

def checkGuess(letter, word):
    if letter.upper() not in word.upper():
        print('\n'+"Wrong")
        return False
        
    else:
        print('\n'+"Yes it's in the word!")
        return True

def updateDisplayWord(word, guessedLetters):
    display = ''
    for letter in word:
        if letter.lower() in guessedLetters:
            display += letter
        else:
            display += '_'
    return display


life = 8

def main():

    global life
    global guessedLetters
    global displayWord
   
    print('\n' + "Welcome to hangman game" + "\n" + "You need to guess the word" + "\n" + "Give me letters and I'll tell you if it's part of the word"
    + "\n" + "you have 8 lives (guesses) and you lose 1 for each wrong guess.")
    hangmanWord = pickWord()
    while life >0: 
        print("Current word: " + displayWord)
        if displayWord.lower() ==  hangmanWord.lower():
            print('\n'+ "Congratulations, you've guessed the word!")
            break
        userGuess = askLetter()
        answer = checkGuess(userGuess, hangmanWord)
        life = loseLife(answer, life)
        displayWord = updateDisplayWord(hangmanWord, guessedLetters)
    
    if life == 0:
        print('\n'+ "Dang it! You lost!")
        print('\n'+ "The word was: " + hangmanWord)
   

main()