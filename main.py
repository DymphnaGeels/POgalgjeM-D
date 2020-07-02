import random
from words import word_list
 
 
def get_word():
   word = random.choice(word_list)
   return word.upper()

def play(word):
   word_completion = "_" * len(word)
   guessed = False
   guessed_letters = []
   guessed_words = []
   tries = 5
   print("Laten we galgje spelen!")
   print('De regels:')
   lijst = ['-na een ingevoerde letter op enter drukken.', '-na vijf foute antwoorden ben je af.']
   for item in lijst:
     print(item)
   print(display_hangman(tries))
   print(word_completion)
   print("\n")
   print('het woord heeft', len(word), 'letters')