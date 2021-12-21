<<<<<<< HEAD
import random

playGame = True
gamesWon = 0
gamesLost = 0

wordsA = open('words_alpha.txt')
word_list = wordsA.read().splitlines()
    
while playGame == True:
    selectedWord = random.choice(word_list).lower()
    lettersGuessed = ""

    guessesAvailable = 7

    while guessesAvailable > 0:
    
        guess = input(f"Your new word is {len(selectedWord)} letter(s) long. Enter a letter or word for your guess: ").lower()
    
        if len(guess) == 1 and guess.isalpha():
            if guess in selectedWord:
                print(f"Correct! {guess} is in the selected word.")
            else:
                guessesAvailable -= 1
                print(f"Incorrect! {guess} is not in the selected word. {guessesAvailable} guess(es) are avaialble.")
        
            lettersGuessed = lettersGuessed + guess
            notGuessedLetters = 0
    
            for letter in selectedWord:
                if letter in lettersGuessed:
                    print(f"{letter}", end="")
                else:
                    print("_", end="")
                    notGuessedLetters += 1
            
            if notGuessedLetters == 0:
                print(f"Congratulations! You have correctly guessed the word {selectedWord}, and have won the game!")
                gamesWon += 1
                break
        elif len(guess) == len(selectedWord) and guess.isalpha():
            if guess == selectedWord:
                print(f"Congratulations! You have correctly guessed the word {selectedWord}, and have won the game!")
                gamesWon += 1
                break
            else:
                guessesAvailable -= 1
                print(f"Incorrect! {guess} is not the selected word. {guessesAvailable} guess(es) are avaialble.")
        else:
            guessesAvailable -= 1
            print(f"This is not a vaild entry. {guessesAvailable} guess(es) are avaialble.")            
    else:
        print(f"You have run out of guesses and have lost the game. The selected word was {selectedWord}. Try again!")
        gamesLost += 1
        
    continueGame = False
    while continueGame == False:
        continuePrompt = input('Would you like to play another round? Yes/No ').lower()
        if continuePrompt == 'yes':
            continueGame = True
            print(f"Get ready for the next round! You have won {gamesWon} game(s) and lost {gamesLost} game(s) so far.")
        elif continuePrompt == 'no':
            print(f"Too bad. You have won {gamesWon} game(s) and lost {gamesLost} game(s). Thank you for playing!")
            quit()
        else:
=======
import random

playGame = True
gamesWon = 0
gamesLost = 0

wordsA = open('words_alpha.txt')
word_list = wordsA.read().splitlines()
    
while playGame == True:
    selectedWord = random.choice(word_list).lower()
    lettersGuessed = ""

    guessesAvailable = 7

    while guessesAvailable > 0:
    
        guess = input(f"Your new word is {len(selectedWord)} letter(s) long. Enter a letter or word for your guess: ").lower()
    
        if len(guess) == 1 and guess.isalpha():
            if guess in selectedWord:
                print(f"Correct! {guess} is in the selected word.")
            else:
                guessesAvailable -= 1
                print(f"Incorrect! {guess} is not in the selected word. {guessesAvailable} guess(es) are avaialble.")
        
            lettersGuessed = lettersGuessed + guess
            notGuessedLetters = 0
    
            for letter in selectedWord:
                if letter in lettersGuessed:
                    print(f"{letter}", end="")
                else:
                    print("_", end="")
                    notGuessedLetters += 1
            
            if notGuessedLetters == 0:
                print(f"Congratulations! You have correctly guessed the word {selectedWord}, and have won the game!")
                gamesWon += 1
                break
        elif len(guess) == len(selectedWord) and guess.isalpha():
            if guess == selectedWord:
                print(f"Congratulations! You have correctly guessed the word {selectedWord}, and have won the game!")
                gamesWon += 1
                break
            else:
                guessesAvailable -= 1
                print(f"Incorrect! {guess} is not the selected word. {guessesAvailable} guess(es) are avaialble.")
        else:
            guessesAvailable -= 1
            print(f"This is not a vaild entry. {guessesAvailable} guess(es) are avaialble.")            
    else:
        print(f"You have run out of guesses and have lost the game. The selected word was {selectedWord}. Try again!")
        gamesLost += 1
        
    continueGame = False
    while continueGame == False:
        continuePrompt = input('Would you like to play another round? Yes/No ').lower()
        if continuePrompt == 'yes':
            continueGame = True
            print(f"Get ready for the next round! You have won {gamesWon} game(s) and lost {gamesLost} game(s) so far.")
        elif continuePrompt == 'no':
            print(f"Too bad. You have won {gamesWon} game(s) and lost {gamesLost} game(s). Thank you for playing!")
            quit()
        else:
>>>>>>> 453c241c7b9eec035c40265c720b6b2bbbe7f729
            print("This is not a valid format. Please enter 'Yes' or 'No' in the prompt")