import spacy #NLP library
import praw
import sys
import requests #Requests data from a URL
from bs4 import BeautifulSoup #Parses HTML content
from collections import Counter #Counts item frequencies in a list
from tabulate import tabulate #Organizes data in a table view
nlp = spacy.load("en")

reddit = praw.Reddit('bot1')

user = reddit.redditor(sys.argv[1])
data = user.comments.new()
text = ''
for comment in data:
    print(comment.body)
    text += comment.body
#Tokenizes the text
tokens = nlp(text)

#Print a small selection of tokens
#print(tokens)
#Print the attributes
table = []
for token in tokens:
  table.append([token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop])

#Use tabulate to create a nicely formatted table
print(tabulate(table, headers=['Text', 'Lemma', 'POS', 'Tag', 'Dep', 'Shape', 'Is Alpha', 'Is Stop']))
words = []
for token in tokens:
#  if not token.is_punct and " " not in token.text:
 if not token.is_punct and " " not in token.text and not token.is_stop:
    words.append(token.text.lower())

top15Words = Counter(words).most_common(15)
print(tabulate(top15Words, headers=['Word', 'Count']))

