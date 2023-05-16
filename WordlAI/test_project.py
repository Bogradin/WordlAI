import requests
from collections import Counter
from operator import itemgetter
import re
import random
import queue
import csv
import time

letters = []

def main():
    meaningpedia_resp = requests.get("https://meaningpedia.com/5-letter-words?show=all")
    pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
    word_list = pattern.findall(meaningpedia_resp.text)

    
    possible_guesses = word_list

    filtered_words = []
    letter_counter(possible_guesses)
    for letter in letters:
        filtered_words = [word for word in possible_guesses if letter in word]
        if not filtered_words:
            continue
        possible_guesses = filtered_words
    
    print(letters)
    print(possible_guesses)

def letter_counter(possible_guesses):
    word_counter = Counter()
    
    for result in possible_guesses:
        word = result.lower().rstrip()
        for letter in set(word):
            word_counter[letter] += 1

    sorted_letters = sorted(word_counter.items(), key=itemgetter(1), reverse=True)

    for letter in sorted_letters:
        letters.append(letter[0])

main()