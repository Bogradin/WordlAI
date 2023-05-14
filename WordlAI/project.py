import requests
from collections import Counter
from operator import itemgetter
import re
import random
#https://gist.github.com/iancward/afe148f28c5767d5ced7a275c12816a3

meaningpedia_resp = requests.get("https://meaningpedia.com/5-letter-words?show=all")
pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
word_list = pattern.findall(meaningpedia_resp.text)

class Wordle():
    def __init__(self, tries, secret_word):
        self.tries = tries
        #self.secret_word = secret_word
        self.secret_word = 'aaccc'
        self.case = 0
    
    def __str__(self):
        if self.case == 1:
            return f"The right word was {self.secret_word}, guessed in {self.tries} tries"
        else:
            return f"The right word was {self.secret_word}, good luck next time!"
        
def main():
    #letter_counter()
    wordle = Wordle(1, select_random_word())
    
    while wordle.tries <= 6:
        guess = input("Guess: ")
        if verify_guess(wordle.secret_word, guess):
            print("🟩🟩🟩🟩🟩")
            wordle.case = 1
            print(wordle)
            return 0
        else:
            matches(wordle.secret_word, guess)
            wordle.tries += 1
    print(wordle)

    
def letter_counter():

    word_counter = Counter()

    for result in word_list:
        word = result.lower().rstrip()
        for letter in set(word):
            word_counter[letter] += 1

    sorted_letters = sorted(word_counter.items(), key=itemgetter(1), reverse=True)

    for letter in sorted_letters:
        print('{}: {}'.format(letter[0], letter[1]))

def select_random_word():
    return random.choice(word_list)

def verify_guess(right_word, guessed_word):
    if (right_word == guessed_word):
        return True
    
def matches(right_word, guessed_word):
    for i in range(5):
        if guessed_word[i] == right_word[i]:
            print("🟩", end = '')
        elif guessed_word[i] in right_word:
            print("🟨", end = '')
        else:
            print("🟥", end = '')
    print("")

if __name__ == "__main__":
    main()