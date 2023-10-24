import random
words = {
    'fiveLetterWords': ['chair', 'table', 'watch', 'skate', 'blend'],
    'sixLetterWords': ['banana', 'bright', 'frozen', 'bucket', 'muffin'],
    'sevenLetterWords': ['amazing', 'journey', 'whistle', 'fantasy', 'rainbow'] 
}

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
        letter = input("Enter a letter of the alphabet as a guess: " + '\n')
        if len(letter) == 1 and letter.isalpha():
            return letter
        else:
            print("Please enter a single letter of the alphabet!" + '\n')

def checkGuess(letter, word):
    if letter.upper() not in word.upper():
        print("Wrong")
        return False
        
    else:
        print("Yes it's in the word!")
        return True

life = 5

def main():

    global life
   
    print("Welcome to hangman game" + "\n" + "you need to guess the a word" + "\n" + "Give me letters and I'll tell you if it's part of the word"
    + "\n" + " you have 5 guesses.")
    hangmanWord = pickWord()
    while life >0: 
        userGuess = askLetter()
        answer = checkGuess(userGuess, hangmanWord)
        life = loseLife(answer, life)
   

main()