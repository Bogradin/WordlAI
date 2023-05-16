import re
import requests

def get_words():
    #https://gist.github.com/iancward/afe148f28c5767d5ced7a275c12816a3
    meaningpedia_resp = requests.get("https://meaningpedia.com/5-letter-words?show=all")
    pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
    return pattern.findall(meaningpedia_resp.text)
    
