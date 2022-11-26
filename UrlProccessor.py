import json
import os
import string
from afinn import Afinn
from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize


class UrlProcessor:
    sentientScores = {}
    afinnScore = 0

    def __init__(self):
        # read output.json file
        with open('output.json', 'r') as f:
            self.data = json.load(f)
        os.chdir("HTML_FILES")
        for item in self.data:
            url = self.processUrl(item['url'])
            # get title from the html page being processed

            with open(item['title'] + '_output.txt', 'w+') as f:
                # remove html tags
                soup = BeautifulSoup(item["html"], 'html.parser')
                text = soup.get_text()
                words = word_tokenize(text)
                self.getAfinnScores(words,item['title'])
                # process the words
                words = word_tokenize(text)
                words = self.processWords(words)
                for word in words:
                    f.write(word + ' ')

    def processWords(self, words):
        words = [word for word in words if word.isalpha()]
        words = [word.lower() for word in words]
        words = [word for word in words if word not in string.punctuation]
        words = [word for word in words if len(word) > 1]
        return words

    def processUrl(self, url):
        url = url.replace("https://", "")
        url = url.replace(".", "")
        url = url.replace("/", "")
        url = url.replace(":", "")
        url = url.replace("www", "")
        url = url.replace("?", "")
        url = url.replace("-", "")
        url = url.replace("=", "")
        return url

    # Getting affin scores but by word because after testing with sentences it always gave me 0.
    # I will use these scores and add them in order to get an overall scores for each cluster later on.
    def getAfinnScores(self, words, url):
        afinn = Afinn()
        for word in words:
            self.afinnScore += afinn.score(word)

        self.sentientScores[url] = self.afinnScore
        self.afinnScore = 0
