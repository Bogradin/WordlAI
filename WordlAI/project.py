import requests
from collections import Counter
from operator import itemgetter
import re
import random
import queue
import csv
#https://gist.github.com/iancward/afe148f28c5767d5ced7a275c12816a3

meaningpedia_resp = requests.get("https://meaningpedia.com/5-letter-words?show=all")
pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
word_list = pattern.findall(meaningpedia_resp.text)

class Wordle():
    def __init__(self):
        self.tries = 0
        self.secret_word = random.choice(word_list)
        #self.secret_word = 'guess'
        self.case = 0
        self.correct = ["", "", "", "", ""]
        self.found = set()
        self.not_possible = set()
        self.letters = []
        self.possible_guesses = word_list
        
    def ai(self):
        filtered_words = []
        for word in self.possible_guesses:
            match = True
            for i in range(5):
                if self.correct[i] and self.correct[i] != word[i]:
                    match = False
                    break
            if match:
                filtered_words.append(word)

        self.possible_guesses = filtered_words
        filtered_words = []

        for word in self.possible_guesses:
            match = True
            for charFound in self.found:
                if charFound not in word:
                    match = False
                    break
            if match:
                filtered_words.append(word)

        self.possible_guesses = filtered_words
        filtered_words = []

        
        for word in self.possible_guesses:
            match = True
            for charNotPossible in self.not_possible:
                if charNotPossible in word:
                    match = False
                    break
            if match:
                filtered_words.append(word)

        self.possible_guesses = filtered_words


    def __str__(self):
        if self.case == 1:
            return f"The right word was {self.secret_word}, guessed in {self.tries + 1} tries"
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

    with open("wordlAI_data.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames = ["won/lose", "secret_word", "guess1", "guess2", "guess3", "guess4", "guess5", "guess6"])
        writer.writerow({"won/lose": 'won_lose', "secret_word": 'secret_word', "guess1": 'guess1', "guess2": 'guess2', "guess3": 'guess3', "guess4": 'guess4', "guess5": 'guess5', "guess6": 'guess6'})
    sample = int(input("sample: "))

    for _ in range(sample):
        wordle = Wordle()
        letter_counter(wordle)
        
        guess = [None, None, None, None, None, None]
        while wordle.tries < 6:
            guess[wordle.tries] = random.choice(wordle.possible_guesses)
            if wordle.verify_guess(guess[wordle.tries]):
                print("🟩🟩🟩🟩🟩")
                wordle.case = 1
                print(wordle)
                break
            else:
                wordle.matches(guess[wordle.tries])
                wordle.tries += 1
                wordle.ai()
        print(wordle)

        with open("wordlAI_data.csv", "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames = ["won/lose", "secret_word", "guess0", "guess1", "guess2", "guess3", "guess4", "guess5"])
            writer.writerow({"won/lose": wordle.case, "secret_word": wordle.secret_word, "guess0": guess[0], "guess1": guess[1], "guess2": guess[2], "guess3": guess[3], "guess4": guess[4], "guess5": guess[5]})
        
    with open("wordlAI_data.csv") as file:
        headerline = next(file)
        total = 0
        for row in csv.reader(file):
            total += int(row[0])
        print(f"Number of games won: {total}")

    
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