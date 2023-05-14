import requests
from collections import Counter
from operator import itemgetter
import re
import random
import queue
#https://gist.github.com/iancward/afe148f28c5767d5ced7a275c12816a3

meaningpedia_resp = requests.get("https://meaningpedia.com/5-letter-words?show=all")
pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
word_list = pattern.findall(meaningpedia_resp.text)

class Wordle():
    def __init__(self):
        self.tries = 1
        self.secret_word = random.choice(word_list)
        #self.secret_word = 'guess'
        self.case = 0
        self.correct = ["", "", "", "", ""]
        self.found = set()
        self.not_possible = set()
        self.letters = []
        
    def ai(self):
        possibilities = word_list
        filtered_words = []
        for word in possibilities:
            match = True
            for i in range(5):
                if self.correct[i] and self.correct[i] != word[i]:
                    match = False
                    break
            if match:
                filtered_words.append(word)

        possibilities = filtered_words
        filtered_words = []

        for word in possibilities:
            match = True
            for charFound in self.found:
                if charFound not in word:
                    match = False
                    break
            if match:
                filtered_words.append(word)

        possibilities = filtered_words
        filtered_words = []

        
        for word in possibilities:
            match = True
            for charNotPossible in self.not_possible:
                if charNotPossible in word:
                    match = False
                    break
            if match:
                filtered_words.append(word)
        possibilities = filtered_words
        print(len(possibilities))
        print(possibilities)


    def __str__(self):
        if self.case == 1:
            return f"The right word was {self.secret_word}, guessed in {self.tries} tries"
        else:
            return f"The right word was {self.secret_word}, good luck next time!"
        
    def matches(self, guessed_word):
        for i in range(5):
            guessedLetter = guessed_word[i]
            if guessedLetter == self.secret_word[i]:
                self.correct[i] = guessedLetter
                remove_from_list(self, guessedLetter)
                print("🟩", end = '')
            elif guessedLetter in self.secret_word:
                self.found.add(guessedLetter)
                remove_from_list(self, guessedLetter)
                print("🟨", end = '')
            else:
                self.not_possible.add(guessedLetter)
                remove_from_list(self, guessedLetter)
                print("🟥", end = '')
        print("")
    
    def verify_guess(self, guessed_word):
        if (self.secret_word == guessed_word):
            return True
        
def main():
    wordle = Wordle()
    letter_counter(wordle)
    
    while wordle.tries <= 6:
        guess = input("Guess: ")
        if wordle.verify_guess(guess):
            print("🟩🟩🟩🟩🟩")
            wordle.case = 1
            print(wordle)
            return 0
        else:
            wordle.matches(guess)
            wordle.tries += 1
            wordle.ai()
    print(wordle)

    
def letter_counter(wordle):
    word_counter = Counter()

    for result in word_list:
        word = result.lower().rstrip()
        for letter in set(word):
            word_counter[letter] += 1

    sorted_letters = sorted(word_counter.items(), key=itemgetter(1), reverse=True)

    for letter in sorted_letters:
        wordle.letters.append(letter[0])

def remove_from_list(wordle, char):
    try:
        wordle.letters.remove(char)
    except: pass

if __name__ == "__main__":
    main()