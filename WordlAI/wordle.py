import random
import dictionary 
word_list = dictionary.get_words()

class Wordle():
    def __init__(self):
        self.tries = 0
        self.secret_word = random.choice(word_list)
        self.correct = ["", "", "", "", ""]
        self.found = []
        self.not_possible = set()
        self.possible_guesses = word_list

    def matches(self, guessed_word):
        for i in range(5):
            guessedLetter = guessed_word[i]
            if guessedLetter == self.secret_word[i]:
                print("🟩", end = '')
            elif guessedLetter in self.secret_word:
                print("🟨", end = '')
            else:
                print("🟥", end = '')
        print("")
    
    def verify_guess(self, guessed_word):
        if (self.secret_word == guessed_word):
            return True
        
    def __str__(self):
        if self.case == 1:
            return f"The right word was {self.secret_word}, guessed in {self.tries + 1} tries"
        else:
            return f"The right word was {self.secret_word}, good luck next time!"
        
def main():
    wordle = Wordle()
    
    while wordle.tries < 6:
        guess = input("guess: ")
        if wordle.verify_guess(guess):
            print("🟩🟩🟩🟩🟩")
            wordle.case = 1
            print(wordle)
            break
        else:
            wordle.matches(guess)
            wordle.tries += 1
    if wordle.case != 1:
        print(wordle)

if __name__ == "__main__":
    main()