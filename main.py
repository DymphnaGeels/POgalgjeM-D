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

   if tries == 5:
    print('je hebt nog 5 beurten over')

   while not guessed and tries > 0:
       guess = input("Typ een letter of een woord:").upper()
       if len(guess) == 1 and guess.isalpha():
           if guess in guessed_letters:
               print("Deze letter heb je al geraden.", guess)
           elif guess not in word:
               print(guess, "zit niet in het woord.")
               tries -= 1
               print('je verliest een beurt, nog', (tries),'beurten over')
               print('je hebt de letters', guessed_letters, 'al geprobeerd')
               guessed_letters.append(guess)
           else:
               print("Goed bezig,", guess, "zit in het woord!")
               guessed_letters.append(guess)
               word_as_list = list(word_completion)
               indices = [i for i, letter in enumerate(word) if letter == guess]
               for index in indices:
                   word_as_list[index] = guess
               word_completion = "".join(word_as_list)
               if "_" not in word_completion:
                   guessed = True
       elif len(guess) == len(word) and guess.isalpha():
           if guess in guessed_words:
               print("Je hebt het woord al geraden", guess)
           elif guess != word:
               print(guess, "is niet het woord.")
               tries -= 1
               print('je verliest een beurt, nog', (tries),'beurten over')
               guessed_words.append(guess)
               used_letters.append(guess)
           else:
               guessed = True
               word_completion = word
       else:
           print("Geen geldige invoer.")
           tries -= 1
           print('je verliest een beurt, nog', (tries),'beurten over')
 
       print(display_hangman(tries))
       print(word_completion)
       print("\n")